# Generated by Django 3.2.7 on 2021-12-25 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0008_topblog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscribe',
            old_name='dob',
            new_name='doc',
        ),
    ]
