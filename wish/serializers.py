from rest_framework import serializers
from wish.models import Item


class ItemSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    modified = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Item
        field = ('name', 'link', 'created', 'modified', 'status')
