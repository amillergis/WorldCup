from django.conf.urls import url
from worldcuppool import views

urlpatterns = [
    url(r'^$', views.get_standings, name='index'),
    url(r'^user/(?P<userID>[0-9]+)/$',views.get_picks, name='user_picks'),
]