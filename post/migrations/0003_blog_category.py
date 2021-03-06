# Generated by Django 3.2.7 on 2021-11-05 10:08

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('post', '0002_delete_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=100)),
                ('cat_icon', models.CharField(max_length=100)),
                ('cat_slug', models.SlugField(max_length=100)),
                ('cat_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('short_desc', models.TextField()),
                ('description', models.TextField()),
                ('doc', models.DateField(auto_now_add=True)),
                ('status', models.BooleanField(blank=True, default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.category')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
