from django.shortcuts import render
from comment.models import Comment
from django.http import JsonResponse

def x(requests):
    description_get= requests.GET.get('description_get')
    blog_id		   = requests.GET.get('blog_id')
    user_id		   = requests.GET.get('user_id')

    Comment.objects.create(
        description= description_get,
        blog_id=blog_id,
        user_id=user_id

        ) 

    return JsonResponse({'status':True}) 
    
