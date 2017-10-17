from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.translation import ugettext_lazy as _
from six import python_2_unicode_compatible

from djangoautoconf.model_utils.len_definitions import TEXT_LENGTH_2048


class ExampleNodeCreateRequest(MPTTModel):
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    content = TextField(max_length=512, blank=True, null=True)


@python_2_unicode_compatible
class TreeItemCreateRequestBaseNode(MPTTModel):
    parent = models.ForeignKey('self', null=True, blank=True)
    name = models.CharField(max_length=TEXT_LENGTH_2048)
    requester = models.ForeignKey(User, null=True, blank=True)
    is_request_to_add = models.BooleanField(default=False)
    created = models.DateTimeField(verbose_name=_(u"Create date"), null=True, auto_now_add=True)

    def __str__(self):
        return "%s->%s" % (str(self.parent), self.name)

    class Meta:
        abstract = True
