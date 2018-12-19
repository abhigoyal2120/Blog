from django.contrib import admin
from .models import Category
from .models import Blog

# from .models import Published_blog 



# admin.site.register(Published_blog)


class BlogAdmin(admin.ModelAdmin):
	list_display=('blog_title','Published_status','published_date')


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category)


#     fieldsets = (
#         ('blog_Title',   {'fields' : ['blog_Title']}),
#         ('Date',    {'fields' : ['pub_date'], 'classes' : ['collapse']}),
#         ('Content', {'fields' : ['content']}),
#     )
#     # list_filter = ['pub_date', 'published']
#     list_filter = ['pub_date']
#     search_fields = ['blog_Title']

