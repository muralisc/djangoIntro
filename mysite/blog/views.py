from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog.views.post_new')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
