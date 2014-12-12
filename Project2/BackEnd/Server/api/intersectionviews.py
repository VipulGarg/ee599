from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView

from friends.models import VennIntersectionData
from api.serializers import VennIntersectionDataSerializer

import facebook
import twitter
import logging
import sys

logger = logging.getLogger(__name__)


class Intersection(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
	logger.debug("Request Received")
	
	
	#For Facebook
	fbtoken = request.GET.get('fbtoken');
	graph = facebook.GraphAPI(fbtoken);
	
	#For Twitter
	token_key = request.GET.get('token');
	token_secret = request.GET.get('token_secret')	
	api = twitter.Api(consumer_key='vX4zFZ2O5EvB2dvVmHKIrZX9f',
              consumer_secret='wuh6s2tU5PCbr9XYv1s9gIb6WnykUbnuEbDSpQ9cia919NvOor',
              access_token_key=token_key,
              access_token_secret=token_secret)

	map_friendListNameFB={}

	my_friends = graph.get_connections("me", "friends")
	fbFriendsCount = len(my_friends['data'])
	for x in range(0, fbFriendsCount):
		friend = my_friends['data'][x]
		map_friendListNameFB[friend['name']] = []
		
	logger.debug("Facebook Friends Received")
	
	my_followers = api.GetFollowers(count=200)
	twitterFollowersCount = len(my_followers)
	intersectionCount = 0
	for x in range(0, twitterFollowersCount):
		follower = my_followers[x]
		if follower.name in map_friendListNameFB:
			intersectionCount = intersectionCount + 1
			logger.debug(follower.name)
		
	logger.debug("Twitter Followers Mapped")
	model1 = VennIntersectionData(idval=1,facebook=fbFriendsCount,twitter=twitterFollowersCount,intersection=intersectionCount)
	serializer = VennIntersectionDataSerializer(model1)
	data = serializer.data
	if 'callback' in request.REQUEST:
		   data = '%s(%s);' % (request.REQUEST['callback'], data)
	logger.debug("Request Completed")
        return Response(data)
