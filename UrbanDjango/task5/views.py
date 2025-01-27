from django.shortcuts import render
from . forms import UserRegister

# псевдо-список существующих пользователей
users = ['user2', 'user4', 'user6']


def is_not_valid_date(info):
    """Проверка правильности заполнения полей"""

    if info['password'] != info['repeat_password']:
        return 'Пароли не совпадают'

    if int(info['age']) < 18:
        return 'Вы должны быть старше 18'

    if info['username'] in users:
        return 'Пользователь уже существует'

    return None


def sign_up_by_html(request):
    """html представление"""
    info = {}
    if request.method == 'POST':
        info['username'] = request.POST.get('username')
        info['password'] = request.POST.get('password')
        info['repeat_password'] = request.POST.get('repeat_password')
        info['age'] = request.POST.get('age')
        info['error'] = is_not_valid_date(info)

    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_django(request):
    """django представление"""
    info = {}
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            info['error'] = is_not_valid_date(info)

    return render(request, 'fifth_task/registration_page.html', context=info)
