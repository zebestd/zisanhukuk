# Generated by Django 3.2.5 on 2021-07-26 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zisanhukuk', '0016_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
