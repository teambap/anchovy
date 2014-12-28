from django.db import models

class Item(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=200)
    link = models.URLField()
    created = models.DateTimeField()
    modified = models.DateTimeField()
    status = models.CharField(max_length=2)




# class DataSerializer(serializers.get_serializer('python')):
#     def get_dump_object(self, obj):
#         return self._current
#
#     def handle_fk_field(self, obj, field):
#         related_ojb = getattr(obj, field.name)
#         value = DataSerializer().serialize([related_ojb])
#         self._current[field.name] = value[0]
#
# class QuerySetSerializer(DataSerializer, serializers.get_serializer('json')):
#     pass
#
# class SingleObjectSerializer(QuerySetSerializer):
#     def serialize(self, obj, **options):
#         return super(SingleObjectSerializer, self).serialize([obj], **options)
#
#     def getvalue(self):
#         value = super(SingleObjectSerializer, self).getvalue()
#         return value.strip('[]\n')