from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def index(request):
    return render(request, 'calculator/index.html')


def count_ingredients(recipe_, servings_):
    return {k: v * int(servings_) for k, v in DATA.get(recipe_).items()}


def do_omlet(request):
    servings = request.GET.get('servings', 1)
    template = 'calculator/index.html'
    context = {'recipe': count_ingredients('omlet', servings)}
    return render(request, template, context)


def do_pasta(request):
    servings = request.GET.get('servings', 1)
    template = 'calculator/index.html'
    context = {'recipe': count_ingredients('pasta', servings)}
    return render(request, template, context)


def do_buter(request):
    servings = request.GET.get('servings', 1)
    template = 'calculator/index.html'
    context = {'recipe': count_ingredients('buter', servings)}
    return render(request, template, context)
