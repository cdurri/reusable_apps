__author__ = 'CIAN'

from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^blog/$', views.post_list),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^pop_posts/$', views.top_posts, name="post_list"),
    url(r'^post/new/$', views.new_post, name='new_post'),
]

