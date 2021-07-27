from django.db import models
from django.contrib.auth.models import User

from django.conf import settings


from django.utils.text import slugify


from django.conf import settings

from django.db.models.signals import pre_save
from django.utils import timezone

from multiselectfield import MultiSelectField


from django import forms
# Create your models here.




class Haber(models.Model):
    isim = models.CharField(max_length=100)
    eklenme_tarihi = models.DateTimeField(auto_now_add=True, null=True)
    aciklama = models.TextField(max_length=10000, null=True)
    dosya = models.FileField(upload_to='', null=True, 
    blank=True)
    resim = models.ImageField(default='faqs.jpg',
                              upload_to='profile_images')
                              

    def __str__(self):
        return self.isim 

COLOR_CHOICES = (
    ('Saglik','Saglik'),
    ('Teknoloji', 'Teknoloji'),
    ('Bilim','Bilim'),
    ('Egitim','Egitim'),
    ('Spor','Spor'),
)

class Post(models.Model):
    user =  models.OneToOneField(User, blank=True, null=True, on_delete=models.CASCADE)
    isim = models.CharField(max_length=200, null=True)
    soru = models.CharField(max_length=255, null=True)
    slug = models.SlugField(null=True)
    kategori= MultiSelectField(choices=COLOR_CHOICES, max_length=1000, max_choices=5)
    aciklama = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.soru

def create_slug(instance, new_slug=None):
    slug = slugify(instance.isim)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


'''
unique_slug_generator from Django Code Review #2 on joincfe.com/youtube/
'''
from .utils import unique_slug_generator

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        # instance.slug = create_slug(instance)
        instance.slug = unique_slug_generator(instance)



pre_save.connect(pre_save_post_receiver, sender=Post)


class Answer(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    isim = models.CharField(max_length=255, null=True)
    kimlik = models.CharField(max_length=250, null=True)
    yanit = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.yanit


def create_slug(instance, new_slug=None):
    slug = slugify(instance.isim)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


'''
unique_slug_generator from Django Code Review #2 on joincfe.com/youtube/
'''
from .utils import unique_slug_generator

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        # instance.slug = create_slug(instance)
        instance.slug = unique_slug_generator(instance)



pre_save.connect(pre_save_post_receiver, sender=Post)


# Answer Model
class Comment(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE, null=True)
    detail=models.TextField(null=True)
    add_time=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.detail


class Yorum(models.Model):
    isim = models.CharField(max_length=100)
    eklenme_tarihi = models.DateTimeField(auto_now_add=True, null=True)
    aciklama = models.TextField(max_length=10000, null=True)
    dosya = models.FileField(upload_to='', null=True, 
    blank=True)
    resim = models.ImageField(default='faqs.jpg',
                              upload_to='profile_images')
                              

    def __str__(self):
        return self.isim 
















class Post(models.Model):
    isim = models.CharField(max_length=200, null=True)
    soru = models.CharField(max_length=255, null=True)
    slug = models.SlugField(null=True)
    aciklama = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.soru

def create_slug(instance, new_slug=None):
    slug = slugify(instance.isim)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


'''
unique_slug_generator from Django Code Review #2 on joincfe.com/youtube/
'''
from .utils import unique_slug_generator

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        # instance.slug = create_slug(instance)
        instance.slug = unique_slug_generator(instance)



pre_save.connect(pre_save_post_receiver, sender=Post)


class Answer(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    isim = models.CharField(max_length=255, null=True)
    yanit = models.TextField(null=True)
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['date_added']

    def __str__(self):
        return self.yanit


def create_slug(instance, new_slug=None):
    slug = slugify(instance.isim)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


'''
unique_slug_generator from Django Code Review #2 on joincfe.com/youtube/
'''
from .utils import unique_slug_generator

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        # instance.slug = create_slug(instance)
        instance.slug = unique_slug_generator(instance)



pre_save.connect(pre_save_post_receiver, sender=Post)


# Answer Model
class Comment(models.Model):
    answer=models.ForeignKey(Answer,on_delete=models.CASCADE, null=True)
    detail=models.TextField(null=True)
    add_time=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.detail
