from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from django.shortcuts import render
from .models import Post

def index(request):
    latest_posts = Post.objects.order_by('-created_at')[:5]
    return render(request, 'index.html', {'latest_posts': latest_posts})
def timeline_view(request):
    if request.method == 'POST':
        content = request.POST.get('content')
        post = Post(content=content, author=request.user)
        post.save()
    posts = Post.objects.all().order_by('-created_at')
    no_ports_message = 'まだ投稿がありません。「新しい投稿」を押して投稿しよう！' if not posts else None
    return render(request, 'view.html', {'posts': posts})
def custom_logout(request):
    logout(request)
    return render(request, 'logout.html')
def index_template(request):
    return render(request, 'index.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/myapp/login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/myapp/login')
    return render(request, 'login.html')