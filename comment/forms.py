from django import forms
from blog.models import Blog
from django.contrib.auth.models import User


class CommentForm(forms.Form):

   # user 	   = forms.ForeignKey(user.models.User, null=True, blank= True)
   # blog		   = forms.ForeignKey(blog.models.Blog,null=True, blank= True)
   user=forms.CharField(
   	widget=forms.Textarea(attrs={'placeholder': 'Please enter the description'}))
   blog=forms.CharField(
   	widget=forms.Textarea(attrs={'placeholder': 'please enter'}))
   description = forms.CharField(
    widget=forms.Textarea(attrs={'placeholder': 'Please enter the  description'}))