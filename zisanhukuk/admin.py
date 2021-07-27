from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Haber)
admin.site.register(Yorum)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Answer)