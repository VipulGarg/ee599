from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView

from friends.models import TimeData, ModelData
from api.serializers import TimeDataSerializer, ModelDataSerializer

import logging
import sys
from datetime import datetime, timedelta
import pickle
import numpy
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures

logger = logging.getLogger(__name__)

class HistoricalData(APIView):
    """
    List all Historical Data
    """
    def get(self, request, format=None):
		logger.debug("Request Received for Historical Views")
		name = request.GET.get('name');
		degree = request.GET.get('degree')
		filename = name + '_' + degree + '.pickle'
		
		with open(filename) as f:
			clf, data_arr = pickle.load(f)
		
		currDate_str = "2014-11-16"
		currDate_tuple = datetime.strptime(currDate_str, "%Y-%m-%d")
		
		n = len(data_arr)
		snippets = set()
		for i in range(10):
			daysDiff = (10 - i) * 14;
			newDate_tuple = currDate_tuple - timedelta(days=daysDiff)
			newDate_str = newDate_tuple.strftime("%Y-%m-%d")
			count = data_arr[i][0]
			newData = TimeData(time=newDate_str, count=count, idval=i)
			snippets.add(newData)
				
		serializer = TimeDataSerializer(snippets, many=True)
		data = serializer.data
		if 'callback' in request.REQUEST:
			   data = '%s(%s);' % (request.REQUEST['callback'], data)
		logger.debug("Request Completed for Historical Views")
		return Response(data)

class PredictedData(APIView):
    """
    Send the Model Data
    """
    def get(self, request, format=None):
		logger.debug("Request Received for Predicted Analysis")
		name = request.GET.get('name');
		degree = request.GET.get('degree')
		filename = name + '_' + degree + '.pickle'
		
		with open(filename) as f:
			clf, data_arr = pickle.load(f)
		
		currDate_str = "2014-11-16"
		currDate_tuple = datetime.strptime(currDate_str, "%Y-%m-%d")
		
		n = len(data_arr)
		snippets = set()
		sumAvgRetweetCount = 0;
		sumDayTweetRatio = 0;
		sumFollowerGrowth = 0;
		for i in range(n):
			sumAvgRetweetCount = sumAvgRetweetCount + data_arr[i][0]
			sumFollowerGrowth  = sumFollowerGrowth + data_arr[i][1]
		
		avgRetweetCount = sumAvgRetweetCount / n;
		followerGrowth = sumFollowerGrowth / n;		
		
		followerStartGrowth = data_arr[n-1][1]
		X = numpy.empty((1, 2))
		poly = PolynomialFeatures(degree=int(degree))
		Predicted_y= []
		lastRetweetCount = data_arr[n-1][0]
		currFollowerGrowth = followerStartGrowth
		for i in range(10):
			list1=[]
			list1.append(lastRetweetCount)
			currFollowerGrowth = currFollowerGrowth + abs((float(followerGrowth)) * currFollowerGrowth)
			list1.append(currFollowerGrowth)
			logger.debug(list1)
			X[0] = list1
			Xpoly = poly.fit_transform(X)
			y = clf.predict(Xpoly)
			Predicted_y.append(int(y[0]))
			lastRetweetCount = int(y[0])
		
		snippets = set()
		for i in range(10):
			daysAdd = (i) * 14;
			newDate_tuple = currDate_tuple + timedelta(days=daysAdd)
			newDate_str = newDate_tuple.strftime("%Y-%m-%d")
			count = Predicted_y[i]
			newData = TimeData(time=newDate_str, count=count, idval=i)
			snippets.add(newData)
				
		serializer = TimeDataSerializer(snippets, many=True)
		data = serializer.data
		if 'callback' in request.REQUEST:
			   data = '%s(%s);' % (request.REQUEST['callback'], data)
		logger.debug("Request Completed for Historical Views")
		return Response(data)

class ModelingData(APIView):
    """
    Send the Model Data
    """
    def get(self, request, format=None):
		logger.debug("Request Received for Modeling Data")
		name = request.GET.get('name');
		degree = request.GET.get('degree')
		filename = name + '_' + degree + '.pickle'
		
		with open(filename, "rb") as f:
			clf, data_arr = pickle.load(f)
		
		currDate_str = "2014-11-16"
		currDate_tuple = datetime.strptime(currDate_str, "%Y-%m-%d")
		
		n = len(data_arr)
		snippets = set()
		sumAvgRetweetCount = 0;
		sumFollowerGrowth = 0;
		for i in range(n):
			sumAvgRetweetCount = sumAvgRetweetCount + data_arr[i][0]
			sumFollowerGrowth  = sumFollowerGrowth + data_arr[i][1] * 100
		
		avgRetweetCount = sumAvgRetweetCount / n;
		followerGrowth = sumFollowerGrowth / n;
		avgRetweetCount = int(avgRetweetCount)
		modeldata = ModelData(count=avgRetweetCount,changeingrowthrate=followerGrowth,idval=1)
		serializer = ModelDataSerializer(modeldata)
		data = serializer.data
		if 'callback' in request.REQUEST:
			   data = '%s(%s);' % (request.REQUEST['callback'], data)
		logger.debug("Request Completed for Historical Views")
		return Response(data)

class WhatIfData(APIView):
    """
    Send the Model Data
    """
    def get(self, request, format=None):
		logger.debug("Request Received for What If Analysis")
		avgRetweetCount = float(request.GET.get('count'));
		followerGrowth = float(request.GET.get('growthrate'));
		name = request.GET.get('name');
		degree = request.GET.get('degree')
		filename = name + '_' + degree + '.pickle'
		
		with open(filename) as f:
			clf, data_arr = pickle.load(f)
		
		currDate_str = "2014-11-16"
		currDate_tuple = datetime.strptime(currDate_str, "%Y-%m-%d")
		
		n = len(data_arr)
		followerStartGrowth = data_arr[n-1][1]
		X = numpy.empty((1, 2))
		poly = PolynomialFeatures(degree=int(degree))
		Predicted_y= []
		lastRetweetCount = avgRetweetCount
		currFollowerGrowth = followerStartGrowth
		for i in range(10):
			list1=[]
			list1.append(lastRetweetCount)
			currFollowerGrowth = currFollowerGrowth + abs((float(followerGrowth) / 100) * currFollowerGrowth)
			list1.append(currFollowerGrowth)
			logger.debug(list1)
			X[0] = list1
			Xpoly = poly.fit_transform(X)
			y = clf.predict(Xpoly)
			Predicted_y.append(int(y[0]))
			lastRetweetCount = int(y[0])
		
		snippets = set()
		for i in range(10):
			daysAdd = (i) * 14;
			newDate_tuple = currDate_tuple + timedelta(days=daysAdd)
			newDate_str = newDate_tuple.strftime("%Y-%m-%d")
			count = int(Predicted_y[i])
			newData = TimeData(time=newDate_str, count=count, idval=i)
			snippets.add(newData)
				
		serializer = TimeDataSerializer(snippets, many=True)
		data = serializer.data
		if 'callback' in request.REQUEST:
			   data = '%s(%s);' % (request.REQUEST['callback'], data)
		logger.debug("Request Completed for Historical Views")
		return Response(data)
