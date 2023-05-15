from django.shortcuts import render
from django.http import HttpResponse


def omlet(request):
    recipe = {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    }
    servings = int(request.GET.get('servings', 1))
    for key in recipe:
        recipe[key] *= servings
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)

def pasta(request):
    recipe = {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    }
    servings = int(request.GET.get('servings', 1))
    for key in recipe:
        recipe[key] *= servings
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)

def buter(request):
    recipe = {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    }
    servings = int(request.GET.get('servings', 1))
    for key in recipe:
        recipe[key] *= servings
    context = {'recipe': recipe}
    return render(request, 'calculator/index.html', context)