from django.db import models


class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250, unique=True)
    content = models.TextField(null=True)
    image = models.ImageField(upload_to="Blog_image")
    video = models.FileField(upload_to="Blog_video",null=True)
    audio = models.FileField(upload_to="Blog_audio",null=True)
    hashtags = models.CharField(max_length=50,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
    

    def __str__(self) :
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100,unique=True)

    def __str__(self) :
        return self.name




class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    


class like(models.Model):
    id = models.AutoField(primary_key=True)
    like = models.BooleanField(default=False)
    blog = models.ForeignKey(Blog,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

# Create your models here.
