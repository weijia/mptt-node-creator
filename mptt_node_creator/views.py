from django.views.generic import TemplateView

from checklist.models import ChecklistTreeItem
from djangoautoconf.model_utils.url_for_models import get_rest_api_url, get_tastypie_api_url
from mptt_node_creator.models import ExampleNodeCreateRequest


class TreeNodeCreator(TemplateView):
    base_tree_model = ChecklistTreeItem
    node_create_request = ExampleNodeCreateRequest
    template_name = 'mptt_node_creator/mptt_node_creator.html'
    root_parent = "None"
    parent_name = "parent"
    display_field = "name"
    query_param = "content__icontains"
    results_field = "objects"

    def get_context_data(self, **kwargs):
        ctx = super(TreeNodeCreator, self).get_context_data(**kwargs)
        ctx["base_tree_url"] = get_tastypie_api_url(self.base_tree_model)
        ctx["root_parent"] = self.root_parent
        ctx["parent_name"] = self.parent_name
        ctx["display_field"] = self.display_field
        ctx["query_param"] = self.query_param
        ctx["results_field"] = self.results_field
        return ctx

