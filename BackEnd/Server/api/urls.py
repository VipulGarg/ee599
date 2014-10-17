from django.conf.urls import patterns, url
from api import views

urlpatterns = patterns(
    '',
    url(r'^friends/$', views.FriendsList.as_view()),
)
