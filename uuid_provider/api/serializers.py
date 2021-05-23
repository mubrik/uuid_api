from rest_framework import serializers
from uuid_provider.models import UidGenerator

class UidSerializer(serializers.ModelSerializer):

    created = serializers.DateTimeField(format='%Y-%m-%d %I:%M:%S.%f')

    class Meta:
        model = UidGenerator
        fields = ['created', 'id']