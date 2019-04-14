from .models import biddings
from rest_framework import serializers
from datetime import datetime
from Myads.models import adProperty
from Myads.Serialisers import AdSlotSerializer
from django.db.models import Max,Q


class biddingsSerializer(serializers.ModelSerializer):
	Valid = serializers.BooleanField(required=False)
	Last_updated =serializers.DateTimeField(required=False)
	Created_on =serializers.DateTimeField(required=False)
	default_columns_ptr =serializers.CharField(required=False)
	# Adid = AdSlotSerializer(required=False)

	class Meta:
		model = biddings
		fields = '__all__'


	def validate(self,data):
		# Validate Data
		return data

	def create(self, validated_data):
		# print (validated_data['Adid'],validated_data)		
		if biddings.objects.filter(Adid=validated_data["Adid"]).exists():
			maxbid = biddings.objects.values("bid_price").filter(Adid=validated_data["Adid"]).order_by("-bid_price")[0]
			if validated_data["bid_price"] <= maxbid["bid_price"]:
				raise serializers.ValidationError("No Content")
		elif not validated_data["open_for_bid"]:
			raise serializers.ValidationError("No Content")
		elif validated_data["bid_price"] < validated_data["Adid"].min_bid_price:
			raise serializers.ValidationError("No Content")
		return biddings.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.bid_price = validated_data.get('bid_price', instance.bid_price)
		instance.Valid = validated_data.get('Valid', instance.Valid)
		instance.Last_updated = datetime.now()
		instance.Created_on = validated_data.get('Created_on', instance.Created_on)
		instance.save()
		return instance


