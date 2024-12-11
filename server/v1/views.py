from django.shortcuts import render, get_object_or_404
from .models import Blog
from django.views import View
def main(request):
    blogs = Blog.objects.all()
    return render(request, 'Blog.html', {"blogs":blogs})

def details(request,pk):
    article = get_object_or_404(Blog, pk=pk)
    return render(request,'details.html', {"article":article})


def contact(request):
    return render(request,'test.html')
# Create your views here.
