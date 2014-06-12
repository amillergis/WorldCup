from django.conf.urls import url
from worldcuppool import views

urlpatterns = [
    url(r'^$', views.get_standings, name='index')
]