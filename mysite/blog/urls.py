from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^login/$', views.lin, name='login'),
    url(r'^create/$', views.create_user, name='create'),
    url(r'^logout/$', views.lout, name='logout'),
]
