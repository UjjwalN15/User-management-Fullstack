from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', landing_page, name='landing-page'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('enterprise_user_home/', enterprise_user_home, name='enterprise_user_home'),
    path('user_home/', user_home, name='user_home'),
    path('create_post/', create_post, name='create_post'),
    path('edit_post/<int:post_id>/', edit_post, name='edit_post'),
    path('delete_post/<int:post_id>/', delete_post, name='delete_post'),
    path('my_posts/', my_posts, name='my_posts'),
    path('dashboard/', dashboard, name='dashboard'),
    path('user_dashboard/', user_dashboard, name='user_dashboard'),
    path('view_post/<int:post_id>/', view_post, name='view_post'),
    path('user_view_post/<int:post_id>/', user_view_post, name='user_view_post'),
    path('like_post/<int:post_id>/', like_post, name='like_post'),
    path('like_post_user/<int:post_id>/', like_post_user, name='like_post_user'),
    path('logout/', logout, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)