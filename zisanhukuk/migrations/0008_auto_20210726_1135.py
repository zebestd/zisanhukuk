# Generated by Django 3.2.5 on 2021-07-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zisanhukuk', '0007_haber_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='haber',
            name='file',
        ),
        migrations.AddField(
            model_name='haber',
            name='dosya',
            field=models.FileField(blank=True, null=True, upload_to='static/files'),
        ),
    ]