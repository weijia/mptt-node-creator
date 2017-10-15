from django.conf.urls import patterns, url
import models
from djangoautoconf.model_utils.url_for_models import add_all_urls
from mptt_node_creator.views import TreeNodeCreator

urlpatterns = patterns('',
                       url(r'^$', TreeNodeCreator.as_view()),
                       )

add_all_urls(urlpatterns, models)
