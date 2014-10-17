from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView

from friends.models import FriendsConnectivity
from api.serializers import FriendsConnectivitySerializer

import twitter
import logging
import sys

logger = logging.getLogger(__name__)


class FriendsList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
	logger.debug("Request Received")
	token_key = request.GET.get('token');
	token_secret = request.GET.get('token_secret')	
	api = twitter.Api(consumer_key='vX4zFZ2O5EvB2dvVmHKIrZX9f',
              consumer_secret='wuh6s2tU5PCbr9XYv1s9gIb6WnykUbnuEbDSpQ9cia919NvOor',
              access_token_key=token_key,
              access_token_secret=token_secret)

	map_followerListScreenName={}
	map_followerListName={}
	map_followerCountToScreenName={}

	currCount = 1
	my_followers = api.GetFollowers()
	num = min(len(my_followers), 14)
	for x in range(0,num):
		follower = my_followers[x]
		map_followerListScreenName[follower.screen_name] = currCount
		map_followerListName[currCount] = follower.name
		map_followerCountToScreenName[currCount] = follower.screen_name
		currCount = currCount + 1
	logger.debug("Inititalization Done")
	i=0
	map_followerConnected={}
	for x in range(0,num):
		follower = my_followers[x]
		try:
			sub_followers = api.GetFollowers(screen_name=follower.screen_name, count=50)
			for sub_follower in sub_followers:
				if sub_follower.screen_name in map_followerListScreenName:
					if follower.screen_name in map_followerConnected:
						map_followerConnected[follower.screen_name].append(map_followerListScreenName[sub_follower.screen_name])
					else:
						map_followerConnected[follower.screen_name] = [map_followerListScreenName[sub_follower.screen_name]]
			i = i + 1
			s = "Successfully Created Mutual Followers for : "
			s += follower.screen_name
			logger.debug(s)
		except:
			s = "Exception for ";
			s += follower.screen_name;
			s += " : "
			logger.debug(s)
		
	logger.debug("Sub Follower Map Done")
	snippets = set()
	for x in range(0,num):
		name1 = 'friends.'
		name1 += map_followerListName[x+1]
		name1 = name1.replace(' ','')
		id=x+1
		if map_followerCountToScreenName[x+1] in map_followerConnected:
			list1 = map_followerConnected[map_followerCountToScreenName[x+1]]
		else:
			list1 = [id]
		c1 = FriendsConnectivity(name=name1,idval=id,size=3,listf=list1)
		logger.debug(name1)
		logger.debug(id)
		logger.debug(list1)
		snippets.add(c1)
			
        #snippets = FriendsConnectivity.objects.all()
        serializer = FriendsConnectivitySerializer(snippets, many=True)
	data = serializer.data
	if 'callback' in request.REQUEST:
		   data = '%s(%s);' % (request.REQUEST['callback'], data)
	logger.debug("Request Completed")
        return Response(data)
