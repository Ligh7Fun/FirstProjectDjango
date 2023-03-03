from django.http import Http404, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from .models import Women, Category


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'cat_selected': 0,
    }

    return render(request, 'women/index.html', context=context)


def about(request):
    context = {
    }

    return render(request, 'women/about.html', context=context)


def addpage(request):
    context = {
    }

    return render(request, 'women/addpage.html', context=context)


def contact(request):
    context = {
    }

    return render(request, 'women/contact.html', context=context)


def login(request):
    context = {
    }

    return render(request, 'women/login.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        'post': post,
        'title': 'Посты',
        'cat_selected': post.cat_id,
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
        'cat_selected': cat_id,
    }

    if request.GET:
        print(request.GET)  # словарь get запросов
    return render(request, 'women/index.html', context=context)


def archive(request, year):
    context = {
    }

    if int(year) > 2023:
        return redirect('home', permanent=False)

    return render(request, 'women/archive.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>404 страница не найдена</h1>')
