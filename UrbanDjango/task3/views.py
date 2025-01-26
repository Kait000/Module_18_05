from django.shortcuts import render


def get_platform(request):
    """Главная страница приложения"""
    return render(request, 'third_task/platform.html')


def get_games(request):
    """Список игр"""
    context = {
        'id_1': 'Oxygen Not Included',
        'id_2': 'Subnautica',
        'id_3': 'Green Hell',
    }
    return render(request, 'third_task/games.html', context)


def get_cart(request):
    """Корзина"""
    return render(request, 'third_task/cart.html')
