from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post
# Create your views here.



def index(request):
    blogs = Post.objects.all()
    return render(
        request, 'blog/index.html', {'post_list':blogs}
    )

def detail(request,pk):
    # def get_object_or_404(Post,pk=pk):
    #     return Post.objects.all()[]
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/detail.html',context={'post':post})