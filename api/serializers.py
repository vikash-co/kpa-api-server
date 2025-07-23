from rest_framework import serializers
from .models import BogieChecksheetForm, WheelSpecificationsForm

class BogieChecksheetFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BogieChecksheetForm
        fields = '__all__'

class WheelSpecificationsFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecificationsForm
        fields = '__all__'
