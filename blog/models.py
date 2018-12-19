from django.db import models
import os
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# from user.models import Role

STATUS_CHOICES = (
    ('n', 'NotPublised'),
    ('p', 'Published'),
    
)


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    ordering            = ('name',)
    verbose_name        = 'category'
    verbose_name_plural = 'categories'
   
    def __str__(self):
        return self.name


class Blog(models.Model):
    # role      = models.ForeignKey(Role, null=True, blank=True)
    
    category    = models.ForeignKey(Category)
    blog_title  = models.CharField(max_length=200)
    Published_status = models.CharField(max_length=1, choices=STATUS_CHOICES, null=True, blank=True)
    image       = models.ImageField(upload_to = 'static/pic_folder/',blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    deleted_at  = models.DateTimeField(blank=True, null=True)
    published_date=models.DateTimeField(blank=True, null=True)



    
    def __str__(self):
        return self.blog_title

    class Meta:
        ordering = ['-created',][0:10]

# class Published_blog(models.Model):
#     published    = models.ForeignKey(Blog)
#     category    = models.ForeignKey(Category)

#     def __str__(self):
#         return self.published




      

        

    