from django.contrib import admin
from .models import Article, Comment

admin.site.register(Article) # Оно регистрируем модели в админку
admin.site.register(Comment)