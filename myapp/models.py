from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.
class Interest(models.Model):
    name=models.TextField(max_length=50)
    def __str__(self):
        return self.name
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    bio=models.CharField(max_length=50,blank=True,default='')
    image=models.ImageField(upload_to='profile_pics',default='profile_pics/default.jpg')
    phone_number=models.CharField(max_length=10, default='')
    dob=models.DateField(default=date.today)
    interests=models.ManyToManyField(Interest,blank=True)
    def __str__(self):
        return self.user.username
class UserPost(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length =50)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title

