# Generated by Django 5.0.6 on 2024-06-05 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_articles_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='article',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='author',
        ),
        migrations.DeleteModel(
            name='dislikes',
        ),
        migrations.DeleteModel(
            name='likes',
        ),
    ]