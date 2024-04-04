from django.shortcuts import render, HttpResponse

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
    # можете добавить свои рецепты ;)
}


def recipes_of_dishes(request, dish):
    servings = int(request.GET.get('servings', 1))
    for k, v in DATA[dish].items():
        DATA[dish][k] = round(v * servings, 2)
    context = {
        'recipe': DATA[dish],
        'recipe1': servings,
        'recipe2': dish,
    }
    return render(request, 'calculator/index.html', context)


def main_page(request):
    return HttpResponse('Главная страница')


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
