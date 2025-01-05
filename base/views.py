from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from .models import *
from django.contrib.auth import update_session_auth_hash
# Create your views here.

def landing_page(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=email, password=password)
        if user is not None:
            auth_login(request, user)
            
            # Get the user's group
            if user.user_type and user.user_type.id == 1:
                # Redirect to enterprise user home
                return redirect('enterprise_user_home')
            elif user.user_type and user.user_type.id == 2:
                # Redirect to user home
                return redirect('user_home')
            else:
                return redirect('login')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('register')
        password = request.POST.get('password')
        hashed_password = password
        user_type = request.POST.get('user-type')
        group = Group.objects.get(name=user_type)
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return redirect('register')
            # Create the user
        my_user = User.objects.create_user(
                email=email,
                password=password,
                hashed_password = hashed_password,
                user_type=group,  # Assign the ForeignKey
            )

        my_user.save()
        return redirect('login')
    return render(request, 'register.html')

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            password = request.POST.get('password')
            user.set_password(password)
            user.hashed_password = password
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password updated Successfully")
            return redirect('login')
        else:
            messages.error(request, "Email not found. Please register.")
            return redirect('register')
    return render(request, 'forgot_password.html')

@login_required(login_url='login')
def logout(request):
    auth_logout(request)
    return redirect('login')

@login_required(login_url='login')
def enterprise_user_home(request):
    posts = Posts.objects.all().order_by('title')
    user = request.user
    context = {
        'posts': posts,
        'user': user,
    }
    return render(request, 'enterprise_user_home.html', context=context)

@login_required(login_url='login')
def user_home(request):
    posts = Posts.objects.all().order_by('title')
    print(posts)
    user = request.user
    context = {
        'posts': posts,
        'user': user,
    }
    return render(request, 'user_home.html', context=context)

@login_required(login_url='login')
def create_post(request):
    if request.method == 'POST':
        user=request.user
        image = request.FILES.get('post-image')
        if image:
            # Save or process the file here
            print(f"Uploaded image: {image.name}")
        else:
            print("No image uploaded")
        title = request.POST.get('post-title')
        description = request.POST.get('post-description')
        new_post = Posts.objects.create(image=image, title=title,author=user, description=description)
        new_post.save()
        return redirect('my_posts')
    return render(request, 'create_post.html')

@login_required(login_url='login')
def my_posts(request):
    user=request.user
    my_posts = Posts.objects.filter(author=user).order_by('title')
    context = {
        'my_posts': my_posts,
        'user': user,
    }
    return render(request, 'my_posts.html', context=context)

@login_required(login_url='login')
def dashboard(request):
    user = request.user
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        if new_password:
            user.set_password(new_password)
            user.hashed_password = new_password
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password updated Successfully")
            return redirect('login')
    context = {
        'user': user,
    }
    return render(request, 'dashboard.html', context=context)

@login_required(login_url='login')
def user_dashboard(request):
    user = request.user
    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        if new_password:
            user.set_password(new_password)
            user.hashed_password = new_password
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password updated Successfully")
            return redirect('login')
    context = {
        'user': user,
    }
    return render(request, 'user_dashboard.html', context=context)

@login_required(login_url='login')
def view_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    post.views += 1
    post.save()
    return render(request, 'view_post.html', context={'post':post})
@login_required(login_url='login')
def user_view_post(request, post_id):
    post = get_object_or_404(Posts, pk=post_id)
    post.views += 1
    post.save()
    return render(request, 'user_view_post.html', context={'post':post})


@login_required(login_url='login')
def like_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    if request.method == 'POST':
        post.clicks += 1
        post.save()
        return redirect('enterprise_user_home')

@login_required(login_url='login')
def like_post_user(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    if request.method == 'POST':
        post.clicks += 1
        post.save()
        return redirect('user_home')

@login_required(login_url='login')
def delete_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    if post.author != request.user:
        messages.error(request, "You are not authorized to delete this post.")
        return redirect('my_posts')
    
    post.delete()
    messages.success(request, f"Post with title {post.title} deleted successfully.")
    return redirect('my_posts')

@login_required(login_url='login')
def edit_post(request, post_id):
    post = get_object_or_404(Posts, id=post_id)
    if request.method == 'POST':
        new_image = request.FILES.get('new-image')
        title = request.POST.get('post-title')
        description = request.POST.get('description')
        if new_image:
            post.image = new_image
        post.title = title
        post.description = description
        post.save()
        messages.success(request, 'Post Updated Successfully')
        return redirect('my_posts')
    return render(request, 'edit_post.html', {'post': post})
