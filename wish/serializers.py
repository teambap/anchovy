from rest_framework import serializers
from wish.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        field = ('name', 'link', 'created', 'modified', 'status')

#
# class ResultSerializer(serializers.ModelSerializer):
#     # result = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
#     items = serializers.SlugRelatedField(
#         many=True,
#         read_only=True,
#         slug_field='name'
#     )
#     class Meta:
#         model = ('code', 'desc')