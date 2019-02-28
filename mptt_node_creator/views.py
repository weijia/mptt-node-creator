from django.views.generic import TemplateView
from djangoautoconf.django_utils import retrieve_param
from djangoautoconf.model_utils.url_for_models import get_tastypie_api_url
from mptt_node_creator.models import ExampleNodeCreateRequest
from mptt_node_creator.tree_table_generator import TreeTableGenerator
from obj_sys.models_ufs_obj import UfsObj


class TreeNodeCreator(TemplateView):
    default_level = 999

    base_tree_model = UfsObj
    node_create_request = ExampleNodeCreateRequest
    # template_name = 'mptt_node_creator/mptt_node_creator_with_tree_view.html'
    template_name = 'mptt_node_creator/mptt_node_creator.html'
    root_parent = "None"
    parent_name = "parent"
    display_field = "content"
    query_param = "content__icontains"
    results_field = "objects"
    max_level_of_input = 9999
    level_names = None

    def init_tree_items(self):
        # super(TreeNodeCreator, self).init_tree_items()
        # self.tree_items = []
        # last_level_items = self.node_create_request.objects.filter(is_request_to_add=True)
        # for item in last_level_items:
        #     self.tree_items.append(item)
        #     while item.parent is not None:
        #         self.tree_items.append(item.parent)
        #         item = item.parent
        self.tree_items = self.node_create_request.objects.filter(is_request_to_add=True)

    def get_context_data(self, **kwargs):
        ctx = super(TreeNodeCreator, self).get_context_data(**kwargs)

        param = retrieve_param(self.request)
        level = 0
        parent = None
        level_parameter_name = "level%d[]" % level
        while level_parameter_name in param:
            level_node_name = param[level_parameter_name]
            parent = self.create_node_creation_request(level_node_name, parent)
            level += 1
            level_parameter_name = "level%d[]" % level

        all_leaf_new_items = self.get_all_new_leaf_nodes()

        ctx["items"] = all_leaf_new_items

        ctx["tree_table"] = TreeTableGenerator(
            self.display_field, self.level_names).get_tree_table(all_leaf_new_items)

        javascript_vars = {
            "base_tree_url": get_tastypie_api_url(self.base_tree_model),
            "root_parent": self.root_parent,
            "parent_name": self.parent_name,
            "display_field": self.display_field,
            "query_param": self.query_param,
            "results_field": self.results_field,
            "max_level_of_input": self.max_level_of_input,
        }

        ctx["javascript_vars"] = javascript_vars
        return ctx

    def get_all_new_leaf_nodes(self):
        all_new_nodes = self.node_create_request.objects.filter(is_request_to_add=True)
        exclude = []
        for item in all_new_nodes:
            if item.parent is not None:
                if item.parent.is_request_to_add:
                    exclude.append(item.parent.id)
        all_new_leaf_nodes = []
        for item in all_new_nodes:
            if item.id in exclude:
                continue
            else:
                all_new_leaf_nodes.append(item)
        return all_new_leaf_nodes

    def create_node_creation_request(self, level_node_name, parent):
        filter_dict = {self.display_field: level_node_name}
        current_level_node_query = self.base_tree_model.objects.filter(**filter_dict)
        create_dict = {self.display_field: level_node_name, "parent": parent}
        obj, is_created = self.node_create_request.objects.get_or_create(**create_dict)
        if not current_level_node_query.exists():
            obj.is_request_to_add = True
        else:
            obj.is_request_to_add = False
        obj.save()
        return obj

