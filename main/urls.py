from django.urls import path
from . import views

urlpatterns = [
    path('', views.initcond, name="initcond"),
    path('initcond', views.initcond, name="initcond"),
    path('model', views.model, name="model"),
    path('visual', views.visual, name="visual"),
    path('pwd', views.pwd, name="pwd"),
    path('delete_init', views.delete_init, name="delete_init"),
    path('delete_calc', views.delete_calc, name="delete_calc"),
]