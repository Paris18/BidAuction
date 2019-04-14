from .models import adProperty
from .Serialisers import AdSlotSerializer
# from rest_framework.decorators import action
from rest_framework import viewsets,status
from rest_framework.response import Response
from .decorators import login_required,user_admin
from django.utils.decorators import method_decorator


class advertisement(viewsets.GenericViewSet):

	@method_decorator(user_admin)
	def get_ad(self, request):
		Adid = request.GET['Adid']
		ad_data = AdSlotSerializer(adProperty.objects.filter(Adid=Adid),many=True)
		return Response(ad_data.data)

	# @method_decorator(user_admin)
	# def leavelistadmin(self, request):
	# 	return Response(SomeModel_json.data)

	@method_decorator(user_admin)
	def insert_for_add(self, request, format='json'):
		serializer = AdSlotSerializer(data=request.data)
		if serializer.is_valid():
			user = serializer.save()
			if user:
				return Response(serializer.data, status=status.HTTP_201_CREATED)
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


	@method_decorator(user_admin)
	def updateAd(self, request, format='json'):
		try:
			ad = request.data
			data = adProperty.objects.get(Adid=ad['Adid'])
			serializer = AdSlotSerializer(data, data=request.data,partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except adProperty.DoesNotExist:
			return Response([{"Status":"Ad Does not Exists"}], status=status.HTTP_204_NO_CONTENT)
		except Exception as e:
			return Response({"status":str(e)}, status=status.HTTP_400_BAD_REQUEST)


	@method_decorator(user_admin)
	def deleteadd(self, request, format='json'):
		try:
			bid = request.data
			bid["Valid"] = False
			data = adProperty.objects.get(Adid=bid['Adid'])
			serializer = AdSlotSerializer(data, data=bid,partial=True)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			else:
				return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		except adProperty.DoesNotExist:
			return Response([{"Status":"Ad Does not Exists"}], status=status.HTTP_204_NO_CONTENT)
		except Exception as e:
			return Response({"status":str(e)}, status=status.HTTP_400_BAD_REQUEST)



