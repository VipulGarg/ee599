from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView

from friends.models import FriendsConnectivity
from api.serializers import FriendsConnectivitySerializer

import facebook
import logging
import sys

logger = logging.getLogger(__name__)


class FriendsList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
	logger.debug("Request Received")
	token = request.GET.get('token');
	graph = facebook.GraphAPI(token);

	map_friendListId={}
	map_friendListName={}
	map_friendCountToId={}

	currCount = 1
	my_friends = graph.get_connections("me", "friends")
	num = len(my_friends['data'])
	for x in range(0,num):
		friend = my_friends['data'][x]
		map_friendListId[friend['id']] = currCount
		map_friendListName[currCount] = friend['name']
		map_friendCountToId[currCount] = friend['id']
		currCount = currCount + 1
	logger.debug("Initialization Done")
	#logger.debug(map_friendListId)
	#logger.debug(map_friendListName)
	#logger.debug(map_friendCountToId)
	i=0
	map_friendConnected={}
	for x in range(0,num):
		friend = my_friends['data'][x]
		try:
			sub_friends = graph.get_connections(friend['id'], "friends")
			total = len(sub_friends['data'])
			for k in range(0,total):
				sub_friend = sub_friends['data'][k];
				#logger.debug(sub_friend)
				if sub_friend['id'] in map_friendListId:
					if friend['id'] in map_friendConnected:
						map_friendConnected[friend['id']].append(map_friendListId[sub_friend['id']])
					else:
						map_friendConnected[friend['id']] = [map_friendListId[sub_friend['id']]]
			i = i + 1
			s = "Successfully Created Mutual Followers for : "
			s += friend['name']
			logger.debug(s)
		except:
			s = "Exception for ";
			s += friend['name'];
			s += " : "
			logger.debug(s)
		
	logger.debug("Sub Friend Map Done")
	#logger.debug(map_friendConnected)
	snippets = set()
	for x in range(0,num):
		name1 = 'friends.'
		name1 += map_friendListName[x+1]
		name1 = name1.replace(' ','')
		id=x+1
		if map_friendCountToId[x+1] in map_friendConnected:
			list1 = map_friendConnected[map_friendCountToId[x+1]]
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
