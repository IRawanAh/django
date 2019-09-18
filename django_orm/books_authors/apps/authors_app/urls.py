from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^book/(?P<id>\d+)$', views.viewBook),
    url(r'^authors$', views.authors),
    url(r'^authors/(?P<id>\d+)$', views.viewAuthors)

]
