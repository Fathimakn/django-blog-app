from django import forms
from .models import UserProfile,UserPost
class UserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=['bio','image','phone_number','dob']
class UserPostForm(forms.ModelForm):
    class Meta:
        model=UserPost
        fields=['title','content']
