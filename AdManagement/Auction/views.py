from django.shortcuts import render

# Create your views here.

from biddings.models import biddings
from Myads.models import adProperty
from biddings.Serialiser import biddingsSerializer
from Myads.Serialisers import AdSlotSerializer
from .Serialiser import AuctioSerializer
# from rest_framework.decorators import action
from rest_framework import viewsets,status
from rest_framework.response import Response
from Myads.decorators import login_required,user_admin
from django.utils.decorators import method_decorator


class auctionapp(viewsets.GenericViewSet):

	@method_decorator(login_required)
	def get_bids(self, request):
		bids = request.query_params
		filterdata = bids.dict()
		if 'Adid' in request.GET:
			filterdata["Adid"] = request.GET["Adid"]
		bid_data = biddingsSerializer(biddings.objects.filter(**filterdata),many=True)
		return Response(bid_data.data)


	@method_decorator(login_required)
	def available_bids(self, request):
		bid_property = request.query_params
		filterdata = bid_property.dict()
		filterdata["open_for_bid"] = True
		if 'Adid' in request.GET:
			filterdata["Adid"] = request.GET["Adid"]
		bid_data = AdSlotSerializer(adProperty.objects.filter(**filterdata),many=True)
		return Response(bid_data.data)

	@method_decorator(login_required)
	def select_bid(self, request, format='json'):
		serializer = AuctioSerializer(data=request.data)
		if serializer.is_valid():
			user = serializer.save()
			if user:
				return Response(serializer.data, status=status.HTTP_200_OK)
			return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)








