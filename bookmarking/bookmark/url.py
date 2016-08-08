from django.conf.urls import url
from . import views

urlpatterns = [
    # /bookmark/ (application to add website address and short descrption)
    url(r'^$', views.input),

    # /bookmark/display?( to display all the bookmarks stored)
    url(r'^display$', views.list_website),

    # /bookmark/search/key (to search the bookmark with given keyword)
    url(r'^search/(?P<key>[A-Za-z0-9]+)/$', views.search),

]
