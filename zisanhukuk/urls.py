from django.urls import include, path
from . import views


from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views


urlpatterns = [
path('', views.home, name='anasayfa'),
path('hakkinda/', views.hakkinda, name='hakkinda'),
path('avukatlik-hizmetleri/', views.avukatlikhizmetleri, name='avukatlik-hizmetleri'),
path('sss/', views.sss, name='sss'),
path('iletisim/', views.iletisim, name='iletisim'),
path('haberler/', views.haberlist, name="haberler"),
path('haber/<str:pk_test>/', views.haber, name="haber"),
path('haberekle/', views.createHaber, name="create_haberler"),
path('haberguncelle/<str:pk>/', views.haberguncelle, name='haberguncelle'),
path('habersil/<str:pk>/', views.habersil, name="habersil"),
path('yorumyap/', views.createYorum, name="create_yorum"),
path('yorumlar/', views.yorumlist, name="yorumlar"),
path('yorum/<str:pk_test>/', views.yorum, name="yorum"),
path('soru/', views.frontpage, name='frontpage'),
path('sorusor/', views.createSoru, name="create_soru"),
path('sorudetay/<int:id>', views.detail, name='detail'),
path('kayit/', views.registerPage, name="register"),
path('giris/', views.loginPage, name="login"),
path('cikis/', views.logoutUser, name="logout"),
path('reset_password/', auth_views.PasswordResetView.as_view (template_name="password_reset.html"), name="reset_password"),
path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"), name="password_reset_done"),
path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"), name="password_reset_confirm"),
path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"), name="password_reset_complete"),
   ] + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)