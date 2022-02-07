from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.Home.as_view(), name="homepage"),
    path('category/', views.Categories.as_view(), name="category"),
    path('subs/', views.SubscribeWork.as_view(), name='subscribe'),
    path('about/', views.About.as_view(), name="about"),
    path('contact/', views.Contact.as_view(), name="contact"),
    path('search/', views.Search.as_view(), name="search"),
    path('terms-and-conditions/', views.Condition.as_view(), name="condition"),
    path('<str:blog_slug>/', views.BlogDetails.as_view(), name="blog"),
    path('tag/<str:tag>/', views.Tags.as_view(), name="tag"),
    path('cat/<str:cat>/', views.CategoryFilter.as_view(), name="category_filter"),

    # Admin work
    path('kcv/', views.AdminLogin.as_view(), name="ad"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
