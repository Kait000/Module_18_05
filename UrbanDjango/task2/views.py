from django.shortcuts import render
from django.views.generic import TemplateView


def main_func(request):
    """функциональное представление"""
    return render(request, 'second_task/func_template.html')


class MainClass(TemplateView):
    template_name = 'second_task/class_template.html'
