from django.shortcuts import render, redirect
from .forms import LoginForm, InitDataForm, CalcDataForm
from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import InitConds, Calculations
from .model import init_start, init_delete, calc_start, calc_delete

# Представление для страницы авторизации пользователя
def pwd(request):
    user = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username='main_user', password=cd['pwd'])

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('initcond'))
        else:
            return render(request, 'main/pwd.html', {'message':'Неправильный код доступа'})
    else:
        form = LoginForm()
    return render(request, 'main/pwd.html', {'form': form})

# Представление для запуска начальных условий
@login_required(login_url=pwd)
def initcond(request):
    data = {
        'id' : '',
        'date' : '',
        'grid' : '',
        'exe' : '',
    }

    init_cond = InitConds.objects.all()
    init_form = InitDataForm()

    if request.method == "POST":
        init_form = InitDataForm(request.POST)
        if init_form.is_valid():
            obj = init_form.save()
            data['id'] = obj.pk
            data['date'] = obj.date
            data['grid'] = obj.grid
            data['exe'] = obj.exe
            
            # Запуск расчёта начальных условий
            init_start.main(data)

    context = {
        'form': init_form,
        'init_cond' : init_cond
    }

    return render(request, 'main/initcond.html', context)

def delete_init(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        item = InitConds.objects.get(pk=item_id)
        item.delete()
        init_delete.main(item_id)

    return redirect('initcond')


# Представление для запуска расчёта модели
@login_required(login_url=pwd)   
def model(request):
    data = {
        'id' : '',
        'init_cond' : '',
        'grid' : '',
        'exe' : '',
        'date' : '',
        'extract_step' : '',
        'ion_step' : '',
        'thermo_step' : '',
        'thermo_type' : '',
        'data_to_load' : '',
    }
    
    calc_form = CalcDataForm()
    init = InitConds.objects.all()
    calc = Calculations.objects.all()

    if request.method == "POST":
        calc_form = CalcDataForm(request.POST)
        if calc_form.is_valid():
            obj = calc_form.save(commit=False)
            init_cond_obj = InitConds.objects.get(id=obj.init_cond.pk)
            init_id = obj.init_cond.pk
            obj.date = init_cond_obj.date
            obj.save()
            data['id'] = obj.pk
            data['date'] = obj.date
            data['init_cond'] = init_id
            data['extract_step'] = obj.extract_step
            data['ion_step'] = obj.ion_step
            data['thermo_step'] = obj.thermo_step
            data['thermo_type'] = obj.thermo_type
            data['data_to_load'] = obj.data_to_load
            data['grid'] = init_cond_obj.grid
            data['exe'] = init_cond_obj.exe
            
            # Запуск основного расчёта
            calc_start.main(data)

    context = {
        'form': calc_form,
        'init' : init,
        'calc' : calc
    }

    return render(request, 'main/model.html', context)

def delete_calc(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        item = Calculations.objects.get(pk=item_id)
        item.delete()
        calc_delete.main(item_id)

    return redirect('model')


@login_required(login_url=pwd)
def visual(request):
    return render(request, 'main/visual.html')