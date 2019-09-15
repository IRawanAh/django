from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^ninja', views.index),
    url(r'^process_money$', views.process),
]
