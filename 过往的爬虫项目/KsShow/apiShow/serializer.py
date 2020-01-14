
from rest_framework import serializers

class SerializerCls(serializers.ModelSerializer):

    class Meta:
        model = None
        fields = '__all__'