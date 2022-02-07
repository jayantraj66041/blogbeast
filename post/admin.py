from django.contrib import admin
from .models import Blog, Category, Subscribe, TopBlog

# Register your models here.
admin.site.register(Subscribe)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'cat_slug': ('cat_name',)}

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(TopBlog)