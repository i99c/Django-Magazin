from django.shortcuts import render, redirect
from .models import *
from .forms import PostForm



def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # Replace 'post_list' with the name of your post list view
    else:
        form = PostForm()
    return render(request, 'Writer/create_post.html', {'form': form})

# Create your views here.




def post_list(request, category_name=None):
    if category_name:
        category = Category.objects.get(name=category_name)
        posts = Post.objects.filter(category=category)
    else:
        posts = Post.objects.all()
    return render(request, 'Writer/news.html', {'posts': posts, 'category_name': category_name})


def news(request):
    return render(request, 'Writer/news.html')





