from django.shortcuts import render, redirect
from django.utils import timezone
from .forms import PostForm
from .models import Post
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def post_list(request):
    if request.user.is_authenticated():
        posts = Post.objects.all()
        return render(request, 'blog/post_list.html', {'posts': posts})
    else:
        return redirect( 'blog.views.lin' )

def post_new(request):
    if request.user.is_authenticated():
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
    else:
        return redirect( 'blog.views.lin' )

def create_user( request ):
    if request.POST:
        u = request.POST['username']
        p = request.POST['password']
        e = request.POST['email']
        user = User.objects.create_user( u, e, p)
        return redirect( 'blog.views.lin' )
    return render(request, 'blog/create.html' )

def lin(request):
    if request.user.is_authenticated():
        return redirect( 'blog.views.post_list' )
    if request.POST:
        print( request.POST )
        u = request.POST['username']
        p = request.POST['password']
        user = authenticate( username=u, password=p )
        if user is not None:
            if user.is_active:
                login( request, user )
                return redirect('blog.views.post_list')
    return render(request, 'blog/login.html', {})

def lout( request ):
    logout( request )
    return redirect( 'blog.views.lin' )
