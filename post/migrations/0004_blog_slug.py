# Generated by Django 3.2.7 on 2021-11-05 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_blog_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
