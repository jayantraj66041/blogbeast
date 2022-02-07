from django.db import models
from taggit.managers import TaggableManager
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_icon = models.CharField(max_length=100, blank=True)
    cat_slug = models.SlugField(max_length=100)
    cat_status = models.BooleanField(default=True)

    def __str__(self):
        return self.cat_name

class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100)
    short_desc = models.TextField()
    description = RichTextField()
    tags = TaggableManager()
    doc = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title

class TopBlog(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog.title

class Subscribe(models.Model):
    email = models.EmailField(max_length=100)
    status = models.BooleanField(default=True)
    doc = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.email
    