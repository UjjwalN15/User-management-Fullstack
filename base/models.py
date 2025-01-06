from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.contrib.auth.models import Group
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=300)
    hashed_password = models.CharField(max_length=300)
    user_type = models.ForeignKey(Group, on_delete=models.CASCADE, related_name="profile", null=True, blank=True)
    skills = models.JSONField(default=list)
    experiences = models.JSONField(default=list)
    
    # Remove the default username field
    username = None
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
class Posts(models.Model):
    image = models.ImageField(upload_to='post_images/')
    title = models.CharField(max_length=300)
    skills = models.JSONField(default=list)
    experiences = models.JSONField(default=list)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    clicks = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)