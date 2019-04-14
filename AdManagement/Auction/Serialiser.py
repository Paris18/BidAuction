from biddings.models import biddings
from rest_framework import serializers
from datetime import datetime
from Myads.models import adProperty
from .models import WinnerBid
from Myads.Serialisers import AdSlotSerializer
from django.db.models import Max,Q


class AuctioSerializer(serializers.ModelSerializer):
	bidid = serializers.PrimaryKeyRelatedField(read_only=True)
	# Adid = AdSlotSerializer(required=False)

	class Meta:
		model = WinnerBid
		fields = '__all__'
		# fields = ('Adid__slot_from','bidid')


	def validate(self,data):
		# Validate Data
		return data

	def create(self, validated_data):
		# print (validated_data['Adid'],validated_data)		
		if biddings.objects.filter(Adid=validated_data["Adid"]).exists():
			maxbid = biddings.objects.values("bid_price").filter(Adid=validated_data["Adid"]).order_by("-bid_price")[0]
			validated_data["bidid"] = validated_data["Adid"].biddings_set.get(bid_price=maxbid["bid_price"])
			validated_data["Adid"].open_for_bid = False
			validated_data["Adid"].save()
			return WinnerBid.objects.create(**validated_data)
		else:
			raise serializers.ValidationError("No Content")



