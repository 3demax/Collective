from django.conf.urls import url

from .views import *


app_name = 'post'
urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^add/$', AddView.as_view(), name="add_post"),
    url(r'^edit/(?P<pk>[\d]+)/$', EditView.as_view(), name="edit_post"),
    url(r'^category/(?P<category_id>[\d]+)/$', CategoryView.as_view(), name="category"),
    url(r'^search/$', SearchView.as_view(), name="search"),
]