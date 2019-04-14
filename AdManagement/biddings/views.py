from .models import biddings
from .Serialiser import biddingsSerializer
# from rest_framework.decorators import action
from rest_framework import viewsets,status
from rest_framework.response import Response
from Myads.decorators import login_required,user_admin
from django.utils.decorators import method_decorator


class biddingsapp(viewsets.GenericViewSet):

	@method_decorator(login_required)
	def get_ad_bid(self, request):
		Adid = request.GET['Adid']
		bid_data = biddingsSerializer(biddings.objects.filter(Adid=Adid).order_by('-bid_price'),many=True)
		return Response(bid_data.data)

	# @method_decorator(user_admin)
	# def leavelistadmin(self, request):
	# 	return Response(SomeModel_json.data)

	@method_decorator(login_required)
	def bid_for_add(self, request, format='json'):
		serializer = biddingsSerializer(data=request.data)
		if serializer.is_valid():
			user = serializer.save()
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_204_NO_CONTENT)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	@method_decorator(login_required)
	def updatebid(self, request, format='json'):
		try:
			bid = request.data
			data = biddings.objects.get(Adid=bid['Adid'])
			serializer = biddingsSerializer(data, data=request.data,partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except biddings.DoesNotExist:
			return Response([{"Status":"Bid_Does not Exists"}], status=status.HTTP_204_NO_CONTENT)
		except Exception as e:
			return Response({"status":str(e)}, status=status.HTTP_400_BAD_REQUEST)


	@method_decorator(login_required)
	def deletebid(self, request, format='json'):
		try:
			bid = request.data
			bid["Valid"] = False
			data = biddings.objects.get(Adid=bid['Adid'])
			serializer = LeaveSerializer(data, data=bid,partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except biddings.DoesNotExist:
			return Response([{"Status":"Bid_Does not Exists"}], status=status.HTTP_204_NO_CONTENT)
		except Exception as e:
			return Response({"status":str(e)}, status=status.HTTP_400_BAD_REQUEST)



