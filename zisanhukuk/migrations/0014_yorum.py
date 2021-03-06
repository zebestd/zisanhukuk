# Generated by Django 3.2.5 on 2021-07-26 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zisanhukuk', '0013_alter_haber_resim'),
    ]

    operations = [
        migrations.CreateModel(
            name='Yorum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
                ('eklenme_tarihi', models.DateTimeField(auto_now_add=True, null=True)),
                ('aciklama', models.TextField(max_length=10000, null=True)),
                ('dosya', models.FileField(blank=True, null=True, upload_to='')),
                ('resim', models.ImageField(default='faqs.jpg', upload_to='profile_images')),
            ],
        ),
    ]
