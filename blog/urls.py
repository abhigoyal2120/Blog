from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.blog_list, name='blog_list'),
   url(r'^blog/(?P<id>\d+)$', views.blog_detail, name='blog_detail'),
   url(r'^detail/$',views.blog_detail, name='blog_detail'),
   url(r'^search/$',views.search_blog, name='search_blog'),
   url(r'^(?P<id>\d+)/$', views.render_category, name='render_category')


] 
