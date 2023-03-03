from django.http import Http404, HttpResponseNotFound
from django.shortcuts import redirect, render
from .models import Women, Category

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить статью', 'url_name': 'add_page'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
    {'title': 'Войти', 'url_name': 'login'},
]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'cat_selected': 0,
    }

    return render(request, 'women/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
    }

    return render(request, 'women/about.html', context=context)


def addpage(request):
    context = {
        'menu': menu,
    }

    return render(request, 'women/addpage.html', context=context)


def contact(request):
    context = {
        'menu': menu,
    }

    return render(request, 'women/contact.html', context=context)


def login(request):
    context = {
        'menu': menu,
    }

    return render(request, 'women/login.html', context=context)


def show_post(request, post_id):
    post = Women.objects.filter(id=post_id)
    print(post)

    if len(post) == 0:
        raise Http404()

    context = {
        'menu': menu,
        'post': post,
        'post_id': post_id,
        'title': 'Посты',
    }

    return render(request, 'women/post.html', context=context)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'cats': cats,
        'menu': menu,
        'cat_selected': cat_id,
    }

    if request.GET:
        print(request.GET)  # словарь get запросов
    return render(request, 'women/index.html', context=context)


def archive(request, year):
    context = {
        'menu': menu,
    }

    if int(year) > 2023:
        return redirect('home', permanent=False)

    return render(request, 'women/archive.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>404 страница не найдена</h1>')
