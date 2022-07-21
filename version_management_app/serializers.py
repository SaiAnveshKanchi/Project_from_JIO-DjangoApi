from rest_framework import serializers

from .models import Version,Data,Device

class VersionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('vv',)
        model = Version

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('dd',)
        model = Device