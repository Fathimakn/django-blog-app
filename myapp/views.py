from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,get_object_or_404
from .models import UserProfile, UserPost
from .forms import UserProfileForm,UserPostForm
from django.contrib.auth.models import User,auth
from django.contrib.auth import login

# Create your views here.
@login_required
def home(request):
    profile,created = UserProfile.objects.get_or_create(user=request.user)
    post=UserPost.objects.filter(user=request.user)
    return render(request, 'home.html', {'profile': profile ,'user': request.user,'post':post})
def logout(request):
    auth.logout(request)
    return redirect('login')
def register(request):
    if request.method=='POST':
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        user_name=request.POST.get('username')
        password_1=request.POST.get('password1')
        password_2=request.POST.get('password2')
        email = request.POST.get('email')
        if password_1==password_2:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=user_name, first_name=first_name ,last_name=last_name ,password=password_1, email=email)
                user.save()
                print('user created')
                profiles=UserProfile.objects.create(user=user)
                login(request,user)
                return redirect('update', id=profiles.id)

        else:
                messages.info(request,'passwords doesnt match')
                return redirect('register')

    else:
        return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
           # profiles = UserProfile.objects.get(user=user)
            #return redirect('update', id=profiles.id)
            return redirect('home')

        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')
def update(request,id):
         profiles= get_object_or_404(UserProfile, id=id)
         if request.method == "POST":
             form = UserProfileForm(request.POST,request.FILES, instance=profiles)
             if form.is_valid():
                 form.save()
                 user=profiles.user
                 user.first_name=request.POST.get('first_name')
                 user.last_name=request.POST.get('last_name')
                 user.email=request.POST.get('email')
                 user.username=request.POST.get('username')
                 # Handle password update (only if provided and not empty)
                 new_password = request.POST.get('password')
                 if new_password:
                     user.set_password(new_password)
                 user.save()

                 return redirect('home')
         else:
             form = UserProfileForm(instance=profiles)

         return render(request, 'update.html', {'form': form, 'profiles': profiles,'user':profiles.user})
def posts(request):
    post=UserPost.objects.all()
    return render(request,'posts.html',{'post': post})
@login_required
def edit_post(request,id):
    post = get_object_or_404(UserPost, id=id,user=request.user)
    if request.method == "POST":
        form = UserPostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')
    else:
        form = UserPostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form})
@login_required
def add_post(request):
    if request.method=="POST":
        form=UserPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user=request.user
            post.save()
            return redirect('posts')
    else:
        form=UserPostForm()
    return render(request,'add_posts.html',{'form':form})




