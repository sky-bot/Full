from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from posts.models import Posts
from datetime import datetime
# Create your views here.
def indexView(request):
    return render(request, 'index.html')

def dashboardView(request):
    return render(request, 'dashboard.html')

def registerView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form })

@login_required
def addPostView(request):
    if request.method == 'POST':
        print(request)
        post = request.POST

        createdAt = datetime.now().replace(microsecond=0)
        
        print("==========================",post)
        
        Posts.objects.create(title=post['title'], subtitle=post['subtitle'], author=post['author'], posts=post['blogcontent'], createdAt=createdAt)

    return render(request, 'addpost.html')




