from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import Category, Blog, TopBlog, Subscribe
from taggit.models import Tag
from django.core.paginator import Paginator

# Create your views here.
class Home(View):
    def get(self, request):
        blogs = Blog.objects.filter(status=True).order_by('-id')
        # print(blogs)
        pg = Paginator(blogs, 5)
        page_number = request.GET.get('page')
        if page_number == '1':
            return redirect('homepage')
        page_obj = pg.get_page(page_number)
        # print("blog", blogs)
        # print("paginator", pg)
        # print("pg_no", page_number)
        # print("page_obj", page_obj)
        return render(request, 'index.html', {
            'categories_list': Category.objects.order_by("?")[:7],
            'blogs': page_obj,
            'top_blog': TopBlog.objects.last(),
            'tags_search': Tag.objects.order_by('?')[:25],
            'tags': Tag.objects.all(),
        })

class Search(View):
    def get(self, request):
        return render(request, 'search.html', {
            'tags_search': Tag.objects.order_by('?')[:25],
        })

class Tags(View):
    def get(self, request, tag):
        blogs = Blog.objects.filter(tags__slug=tag, status=True).order_by('-id')
        paginator = Paginator(blogs, 5)
        page_no = request.GET.get('page')
        if page_no == '1':
            return redirect('tag', tag)
        blogs_obj = paginator.get_page(page_no)
        return render(request, 'tags.html', {
            'tag': Tag.objects.get(slug = tag),
            'tags_search': Tag.objects.order_by('?')[:25],
            'blogs': blogs_obj,
        })

class CategoryFilter(View):
    def get(self, request, cat):
        blogs = Blog.objects.filter(category__cat_slug=cat, status=True).order_by('-id')
        paginator = Paginator(blogs, 5)
        page_no = request.GET.get('page')
        if page_no == '1':
            return redirect('category_filter', cat)
        blogs_obj = paginator.get_page(page_no)
        return render(request, 'category_filter.html', {
            'blog_filter': blogs_obj,
            'category_name': Category.objects.get(cat_slug=cat),
            'tags_search': Tag.objects.order_by('?')[:25],
        })

class BlogDetails(View):
    def get(self, request, blog_slug):
        category = Blog.objects.get(slug=blog_slug).category
        return render(request, 'blog.html', {
            'tags_search': Tag.objects.order_by('?')[:25],
            'blog': Blog.objects.get(slug=blog_slug, status=True),
            'related_blog': Blog.objects.filter(status=True, category=category).exclude(slug=blog_slug)[:10],
        })

class Categories(View):
    def get(self, request):
        return render(request, 'category.html', {
            'tags_search': Tag.objects.order_by('?')[:25],
            'categories': Category.objects.all(),
        })

class SubscribeWork(View):
    def post(self, request):
        find_subscriber = Subscribe.objects.filter(email=request.POST.get("email"), status=True).count()
        if find_subscriber > 0:
            return HttpResponse("exists")
        else:
            sub = Subscribe()
            sub.email = request.POST.get("email")
            sub.save()
            return HttpResponse("success")
    def get(self, request):
        print("hello")
        return HttpResponse("fail")

class About(View):
    def get(self, request):
        return render(request, 'about.html', {
            'tags_search': Tag.objects.order_by('?')[:25],
        })

class Contact(View):
    def get(self, request):
        return render(request, 'contact.html', {
            'tags_search': Tag.objects.order_by('?')[:25],
        })

class Condition(View):
    def get(self, request):
        return render(request, 'condition.html', {
            'tags_search': Tag.objects.order_by('?')[:25],
        })

# Admin work

class AdminLogin(View):
    def get(self, request):
        return render(request, 'writer/login.html')