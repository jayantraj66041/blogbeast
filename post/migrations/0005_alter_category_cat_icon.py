# Generated by Django 3.2.7 on 2021-11-05 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='cat_icon',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
