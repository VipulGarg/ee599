from django.conf.urls import patterns, url
from api import twitterviews
from api import facebookviews
from api import modelingviews
from api import intersectionviews

urlpatterns = patterns(
    '',
    url(r'^twitter/friends/$', twitterviews.FriendsList.as_view()),
    url(r'^facebook/friends/$', facebookviews.FriendsList.as_view()),
    url(r'^modeling/historical/$', modelingviews.HistoricalData.as_view()),
    url(r'^modeling/predicted/$', modelingviews.PredictedData.as_view()),
    url(r'^modeling/whatif/$', modelingviews.WhatIfData.as_view()),
    url(r'^modeling/model/$', modelingviews.ModelingData.as_view()),
    url(r'^intersection/$', intersectionviews.Intersection.as_view()),
)
