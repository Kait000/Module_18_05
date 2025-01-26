from django.shortcuts import render


def get_platform(request):
    """Главная страница приложения"""
    return render(request, 'fourth_task/platform.html')


def get_games(request):
    """Список игр"""
    context = {'games': [
        'Oxygen Not Included',
        'Subnautica',
        'Green Hell',
    ]}
    return render(request, 'fourth_task/games.html', context)


def get_cart(request):
    """Корзина"""
    return render(request, 'fourth_task/cart.html')
