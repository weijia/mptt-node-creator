from django_tables2 import Column
from django_tables2_reports.tables import TableReport


class TreeTableGenerator(object):
    """
    Generate the following table class:
        class XxxxxAutoTable(TableReport):
            level0 = Column()
            level1 = Column()
            level2 = Column()
            level3 = Column()
            level4 = Column()
            class Meta:
                model = Xxxxx
                exclude = []
        :return:
    """
    max_level = 5

    def __init__(self, display_field):
        super(TreeTableGenerator, self).__init__()
        self.display_field = display_field

    def get_tree_table(self, tree_nodes):
        field_list = {}
        for i in xrange(self.max_level):
            field_list["level%d" % i] = Column()
        table_class = type("AutoTreeTable", (TableReport,), field_list)
        # data = [{
        #     "level0": "node0",
        #     "level1": "node0",
        #     "level2": "node0",
        #     "level3": "node0",
        #     "level4": "node0",
        #         }]
        data = []
        for leaf in tree_nodes:
            level = self.max_level-1
            res = {}
            while leaf.parent is not None:
                res["level%d" % level] = getattr(leaf, self.display_field)
                leaf = leaf.parent
                level -= 1
            res["level%d" % level] = getattr(leaf, self.display_field)
            data.append(res)
        return table_class(data)
