from django.utils import timezone
from rest_framework import serializers
from wish.models import Item


class ItemSerializer(serializers.ModelSerializer):
    # created = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')
    created = serializers.DateTimeField()
    modified = serializers.DateTimeField()
    # print(created)
    # created = timezone.localtime(created)

    # print(timezone.get_current_timezone())
    # modified = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S', default_timezone=timezone.get_current_timezone())
    # modified = serializers.DateTimeField(default_timezone=timezone.get_current_timezone())

    class Meta:
        model = Item
        field = ('name', 'link', 'created', 'modified', 'status',)
        exclude = ('user_id',)
