# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-25 12:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zisanhukuk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=255, null=True)),
                ('kimlik', models.CharField(max_length=250, null=True)),
                ('yanit', models.TextField(null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['date_added'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField(null=True)),
                ('add_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('answer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zisanhukuk.Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=200, null=True)),
                ('soru', models.CharField(max_length=255, null=True)),
                ('slug', models.SlugField(null=True)),
                ('kategori', multiselectfield.db.fields.MultiSelectField(choices=[('Saglik', 'Saglik'), ('Teknoloji', 'Teknoloji'), ('Bilim', 'Bilim'), ('Egitim', 'Egitim'), ('Spor', 'Spor')], max_length=1000)),
                ('aciklama', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
        migrations.RemoveField(
            model_name='usta',
            name='user',
        ),
        migrations.DeleteModel(
            name='Usta',
        ),
        migrations.AddField(
            model_name='answer',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zisanhukuk.Post'),
        ),
    ]