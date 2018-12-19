from django.shortcuts import render
from blog.models import Category, Blog
from comment.models import Comment

# Create your views here.
def blog_list(request):
    
    catogories = Category.objects.all()
    blogs      = Blog.objects.filter(Published_status='p')
    search_term = request.GET.get('search_term', None)
    
    return render(request,'front.html',{"catogories":catogories,"blogs":blogs})
    
        
def blog_detail(request,id):
    catogories = Category.objects.all()
    blog   = Blog.objects.get(pk=id)
    comments = Comment.objects.filter(blog=id)
    
    return render(request,'secondblog.html',{"catogories": catogories,"blog":blog, "comments":comments})     


def search_blog(request):
    print("oinnn")
    search_term =request.GET.get('search_term')
    searched_blog= Blog.objects.filter(blog_title=search_term)
   
    # import pdb;pdb.set_trace();
    return render(request,'front.html',{"blogfound":True,"searched_blog":searched_blog})
  
    
def render_category(request,id):
    print(id)
    blogs = Blog.objects.filter(category_id=id)
    # import pdb;pdb.set_trace();   
    return render(request,'render.html',{"blogs":blogs})     

def bad_request(request):
    response = render_to_response(
        '400.html',
        context_instance=RequestContext(request)
        )

    response.status_code = 400

    return response
   
   
   



    


    

    
     