from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post, Category, Tag
# Create your views here.



def index(request):
    blogs = Post.objects.all().order_by('created_time')
    lasted_blogs = []
    if len(blogs) > 4:
        lasted_blogs = blogs[:4]
    else:
        lasted_blogs = blogs

    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(
        request, 'blog/index.html', {
            'post_list' : blogs,
            'lasted_blogs' : lasted_blogs,
            'category' : categories,
            'tags' : tags,
        }
    )


def full_list(request):
    blogs = Post.objects.all().order_by('created_time')
    return render(
        request, 'blog/full-width.html', {
            'post_list' : blogs,
        }
    )

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/detail.html',context={'post':post})