from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {
        'text': "Это главная страница проекта Yatube"
    }
    return render(request, 'posts/index.html', context)

def group_posts(request):
    context = {
        'text': "Здесь будет информация о группах проекта Yatube"
    }
    return render(request, 'posts/group_list.html', context)

def post_detail(request, pk):
    return HttpResponse(f'Страница c новостью {pk}')
