from django.urls import path
from . import views


urlpatterns = [
    path('func_template', views.main_func),
    path('class_template', views.MainClass.as_view()),
]
