from lib2to3.fixes.fix_input import context

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
@login_required
def create_post(request):
    if request.method == 'GET':
        context = {'form': PostForm()}
        return render(request, 'post/post_form.html', context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request, 'post/post_form.html',{'form':form})

def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'post/home.html', context)


def about(request):
    return render(request, 'blog/about.html')

# def about(request):
#     return  render(request, 'blog/about.html')
def edit_post(request, id):
    post= get_object_or_404(Post, id=id)
    if request.method =="GET":
        context = {'form':PostForm(instance=post), 'id':id}
        return  render(request, 'post/post_form.html', context)
    elif request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пост успешно изменен')
            return redirect('posts')
        else:
            messages.error(request, 'Проверьте введённые данные, ошибка!')
            return render(request,'post/post_form.html', {'form':form})
@login_required
def delete_post(request, id):
    post= get_object_or_404(Post, id=id)
    context = {'post':post}
    if request.method == 'GET':
        return render(request, 'post/post_delete.html', context)
    elif request.method == "POST":
        post.delete()
        messages.success(request, 'Посто успешно удалён')
        return redirect('home')