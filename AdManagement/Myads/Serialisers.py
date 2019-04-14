from .models import adProperty
from rest_framework import serializers
from datetime import datetime


class AdSlotSerializer(serializers.ModelSerializer):
	Valid = serializers.BooleanField(required=False)
	Last_updated =serializers.DateTimeField(required=False)
	Created_on =serializers.DateTimeField(required=False)
	open_for_bid =serializers.BooleanField(required=False)
	min_bid_price =serializers.FloatField(required=False)
	default_columns_ptr =serializers.CharField(required=False)

	class Meta:
		model = adProperty
		fields = '__all__'


	def validate(self,data):
		# Validate Data
		return data

	def create(self, validated_data):
		return adProperty.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.slot_Name = validated_data.get('slot_Name', instance.slot_Name)
		instance.slot_from = validated_data.get('slot_from', instance.slot_from)
		instance.slot_to = validated_data.get('slot_to', instance.slot_to)
		instance.open_for_bid = validated_data.get('open_for_bid', instance.open_for_bid)
		instance.min_bid_price = validated_data.get('min_bid_price', instance.min_bid_price)
		instance.Valid = validated_data.get('Valid', instance.Valid)
		instance.Last_updated = datetime.now()
		instance.save()
		return instance


