from django.contrib import admin
from .models import Blog
from .models import Comment
from .models import like



class Blogadmin(admin.ModelAdmin):
    list_display = ['id',"title","image","created_at"]
    list_filter = ["created_at"]
    search_fields = ["title","content"]

admin.site.register(Blog, Blogadmin)


class commentsadmin(admin.ModelAdmin):
    list_display = ['id','blog','content','created_at']
    list_filter = ["created_at"]
    search_fields = ['content']

admin.site.register(Comment, commentsadmin)

class likeadmin(admin.ModelAdmin):
    list_display = ['id','blog','like','created_at']
    list_filter = ["created_at"]

admin.site.register(like, likeadmin)


# Register your models here.
