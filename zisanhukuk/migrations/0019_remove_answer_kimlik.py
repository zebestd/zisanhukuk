# Generated by Django 3.2.5 on 2021-07-26 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('zisanhukuk', '0018_remove_post_kategori'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='kimlik',
        ),
    ]
