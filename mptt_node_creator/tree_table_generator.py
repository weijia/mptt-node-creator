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

    def __init__(self, display_field, level_names=None):
        super(TreeTableGenerator, self).__init__()
        self.display_field = display_field
        self.level_names = level_names

    def get_tree_table(self, tree_nodes):
        field_list = {}
        for i in xrange(self.max_level):
            field_list[self.get_level_name(i)] = Column(verbose_name=self.get_level_verbose(i))
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
                res[self.get_level_name(level)] = getattr(leaf, self.display_field)
                leaf = leaf.parent
                level -= 1
            res[self.get_level_name(level)] = getattr(leaf, self.display_field)
            data.append(res)
        return table_class(data)

    def get_level_verbose(self, level):
        if self.level_names is None:
            return self.get_level_name(level)
        else:
            return self.level_names[level]

    def get_level_name(self, level):
        return "level%d" % level
