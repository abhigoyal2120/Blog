from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^comment/$', views.x, name='x'),
]