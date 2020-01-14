from rest_framework import serializers

from .models import GushiInfo


class GushiSerializer(serializers.ModelSerializer):

    class Meta:
        model = GushiInfo
        fields = '__all__'


