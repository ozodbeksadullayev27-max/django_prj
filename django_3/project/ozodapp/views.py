from django.shortcuts import render,redirect
from .models import Post,Category
from django.db.models import Q
from .forms import RegisterForm 

# Create your views here.


def base(request):
    return render(request,'ozodapp/base.html')

def home(request):
    category = Category.objects.order_by('-date')[:8]
    posts = Post.objects.all()
    last_posts = Post.objects.order_by('-date')[:3]
    pop_news = Post.objects.filter(popular__gte = 10000)[:3]
    context = {
        'posts':posts,
        'last_posts':last_posts,
        'category':category,
        'pop_news':pop_news
    }
    return render(request,'ozodapp/home.html',context)

def post_detail(request,slug):
    post_detail = Post.objects.get(slug=slug)
    post_detail.popular +=1
    post_detail.save()
    context = {
        'post_detail':post_detail
    }
    return render(request,'ozodapp/post_detail.html',context)

def category_detail(request,slug):
    category_detail = Category.objects.get(slug=slug)
    category = category_detail.category_set.order_by('-date')
    context = {
        'category_detail':category_detail,
        'category':category
    }
    return render(request,'ozodapp/category_detail.html',context)

def search(request):
    query = request.GET.get('search_title')
    search_objs = Post.objects.filter(
        Q(title__icontains = query) | Q(info__icontains = query)
    )
    context = {
        'query':query,
        'search_objs':search_objs
    }
    return render(request,'ozodapp/search.html',context)

def register(request):
    if request.method == 'Post':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # log the user in
            return redirect('home')
    else:
        form = RegisterForm()
    return render (request,'ozodapp/register.html',{'form':form})
