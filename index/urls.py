from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^index/$',views.index),
    url(r'^goodlist(\d+)_(\d+)_(\d+)/$',views.goodlist),
    url(r'^list/id=(\d+)/pageid=(\d)/$',views.list),

]