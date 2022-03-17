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


def omlet_view(request, recipe):
    context = {'recipe': counting_ingredients(recipe, request)}
    return render(request, 'calculator/index.html', context)


def counting_ingredients(recipe, dict):
    try:
        return {key: val * serving_definition(dict) for key, val in DATA[recipe].items()}
    except:
        return None


def serving_definition(dict):
    try:
        return int(dict.GET.get('servings'))
    except:
        return 1
