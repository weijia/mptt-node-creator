from django.db.models import TextField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class ExampleNodeCreateRequest(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    content = TextField(max_length=512, blank=True, null=True)
