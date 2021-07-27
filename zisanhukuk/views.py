from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user

from django.contrib.auth.models import User

from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse, HttpResponse

from django.db.models import Q

# from .filters import *

def home(request):
    return render(request, 'index.html')

def hakkinda(request):
    return render(request, 'hakkinda.html')

def avukatlikhizmetleri(request):
    return render(request, 'avukatlik-hizmetleri.html')

def sss(request):
    return render(request, 'sss.html')

def iletisim(request):
    return render(request, 'iletisim.html')

# Create your views here.
@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Basariyla kayit oldunuz ' +
                             user + '. Devam etmek icin lutfen giris yapin.')

            return redirect('login')
    context = {'form': form}
    return render(request, 'register.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('anasayfa')
        else:
            messages.info(
                request, 'kullanici adi VEYA parolayi yanlis girdiniz')
    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def haber(request, pk_test):
        habers = Haber.objects.get(id=pk_test)
        context = {'habers':habers}
        return render(request, 'haber.html',context) 

def haberlist(request):
    haber = Haber.objects.all().order_by('-eklenme_tarihi')


#girisimFilter = GirisimFilter(request.GET, queryset=girisimci)
#girisimci = girisimFilter.qs

    return render(request, 'haberler.html', {'haber':haber})


#@login_required(login_url='login')
def createHaber(request):
    form = HaberForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = HaberForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'haberform.html', context)

def haberguncelle(request, pk):

	haberis = Haber.objects.get(id=pk)
	form = HaberForm(instance=haberis)

	if request.method == 'POST':
		form = HaberForm(request.POST, instance=haberis)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'haberform.html', context)


def habersil(request, pk):
	haber = Haber.objects.get(id=pk)
	if request.method == "POST":
		haber.delete()
		return redirect('/')

	context = {'item':haber}
	return render(request, 'sil.html', context)

def createYorum(request):
    form = YorumForm()
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = YorumForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'yorumform.html', context)

def yorumlist(request):
    yorum = Yorum.objects.all().order_by('-eklenme_tarihi')

    return render(request, 'yorumlar.html', {'yorum':yorum})

def yorum(request, pk_test):
        yorums = Yorum.objects.get(id=pk_test)
        context = {'yorums':yorums}
        return render(request, 'yorum.html',context) 



#Sorya

def frontpage(request):
    posts = Post.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        posts=Post.objects.annotate(total_comments=Count('answer__comment')).filter(Q(soru__icontains=q)|Q(aciklama__icontains=q)|Q(isim__icontains=q)).order_by('-date_added')
    else:
        posts=Post.objects.annotate(total_comments=Count('answer__comment')).all().order_by('-id')
    paginator=Paginator(posts,10)
    page_num=request.GET.get('page',1)
    posts=paginator.page(page_num)
    

    return render(request, 'soryafrontpage.html', {'posts': posts})


def createSoru(request):
    form = SoruForm()
    posts = Post.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        posts=Post.objects.annotate(total_comments=Count('answer__comment')).filter(Q(soru__icontains=q)|Q(aciklama__icontains=q)|Q(isim__icontains=q)).order_by('-date_added')
        return render(request, 'soryafrontpage.html', {'posts': posts})
    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = SoruForm(request.POST)
        if form.is_valid():
            kategori = form.cleaned_data.get('kategori')
            instance = form.save(commit=False)
            if request.user.is_authenticated:
                instance.user = request.user
                instance.save()
                form.save()
            else:
                form.save()
            return redirect('/soru/')
    context = {'form':form}
    return render(request, 'soryaform.html', context)


def detail(request,id):
    posts = Post.objects.all()
    if 'q' in request.GET:
        q=request.GET['q']
        posts=Post.objects.annotate(total_comments=Count('answer__comment')).filter(Q(soru__icontains=q)|Q(aciklama__icontains=q)|Q(isim__icontains=q)).order_by('-date_added')
        return render(request, 'soryafrontpage.html', {'posts': posts})
    quest=Post.objects.get(pk=id)
   # tags=quest.kategori.split(',')
    answers=Answer.objects.filter(post=quest).order_by('-date_added')
    
    form = CommentForm
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = quest
            comment.save()
            
    else:
        form = CommentForm()
    return render(request,'soryaquestdetail.html',{
        'quest':quest,
       # 'tags':tags,
        'answers':answers,
        'form':form,
    })


# Save Comment
def save_comment(request):
    if request.method=='POST':
        comment=request.POST['comment']
        answerid=request.POST['answerid']
        answer=Answer.objects.get(pk=answerid)
        user=request.user
        Comment.objects.create(
            answer=answer,
            comment=comment,
            user=user
        )
        return JsonResponse({'bool':True})
