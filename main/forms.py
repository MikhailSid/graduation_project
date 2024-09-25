from django import forms
from .models import InitConds, Calculations
from django.forms import ModelForm, DateTimeInput, RadioSelect, CheckboxSelectMultiple

class LoginForm(forms.Form):
    pwd = forms.CharField(label='Код доступа')

class InitDataForm(ModelForm):
    class Meta:
        model = InitConds
        fields = ['date', 'grid', 'exe']
        grid_choices = [('05', '5°'),('10', '10°'),('15', '15°')]
        exe_choices = [('standart', 'Стандартная версия'), ('MFACE_dipole', 'MFACE_dipole')]

        widgets = {
            "date": DateTimeInput(attrs={
            'class': 'form-control',
            'type': 'date'
            }),

            "grid": RadioSelect(attrs={
                'class': 'form-check-inline text-start',
            }, choices=grid_choices),

            "exe": RadioSelect(attrs={
                'class': 'form-check-inline text-start',
            }, choices=exe_choices)
        }

class CalcDataForm(ModelForm):
    class Meta:
        model = Calculations
        fields = ['extract_step', 'ion_step', 'thermo_step', 'thermo_type', 'data_to_load', 'init_cond']
        init_choices = [(el.pk, el.date) for el in InitConds.objects.all()]
        extract_choices = [('30', '30 минут'), ('60', '60 минут')]
        ion_choices = [('6', '6 секунд'), ('12', '12 секунд'), ('18', '18 секунд'), ('24', '24 секунды'), ('36', '36 секунд'), ('60', '60 секунд')]
        thermo_choices = [('6', '6 секунд'), ('12', '12 секунд'), ('18', '18 секунд'), ('24', '24 секунды'), ('36', '36 секунд'), ('60', '60 секунд')]
        type_choices = [('theor', 'Теоретический'), ('imper', 'Эмпирический')]
        data_to_load_choices = [('N(O2)','N(O2)'), ('N(N2)','N(N2)'), ('N(O)','N(O)'), ('N(NO)','N(NO)'), ('N(N)','N(N)'), ('N(XY+)','N(XY+)'), ('Tn','Tn'),
                                ('Ti','Ti'), ('Te','Te'), ('Vr','Vr'), ('Vt','Vt'), ('Vd','Vd'), ('q(O2+)','q(O2+)'), ('q(N2+)','q(N2+)'),
                                ('q(NO+)','q(NO+)'), ('q(O+)','q(O2+)'), ('pot','pot'), ('N(O+)','N(O+)'), ('Vr(O+)','Vr(O+)'), ('Vt(O+)','Vt(O+)'), ('Vd(O+)','Vd(O+)')
                                ]

        widgets = {
            "init_cond": RadioSelect(attrs={
                'class': 'text-start',
            }, choices=init_choices),

            "extract_step": RadioSelect(attrs={
                'class': 'form-check-inline; text-start',
            }, choices=extract_choices),

            "ion_step": RadioSelect(attrs={
                'class': 'form-check-inline; text-start',
            }, choices=ion_choices),

            "thermo_step": RadioSelect(attrs={
                'class': 'form-check-inline; text-start',
            }, choices=thermo_choices),

            "thermo_type": RadioSelect(attrs={
                'class': 'form-check-inline; text-start',
            }, choices=type_choices),

            "data_to_load": CheckboxSelectMultiple(attrs={
                'class': 'checkbox-columns',
                'name': 'loaddata'
            }, choices=data_to_load_choices),

        }