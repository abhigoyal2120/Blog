from django.db import models
from blog.models import Blog
from django.contrib.auth.models import User


class Comment(models.Model):
    user            = models.ForeignKey(User, null=True, blank= True)
    blog        	= models.ForeignKey(Blog,null=True, blank= True)
    description     = models.TextField(max_length=255)
    date            = models.DateField(auto_now_add=True)
    
def __str__(self):
        return description
   

     
 
