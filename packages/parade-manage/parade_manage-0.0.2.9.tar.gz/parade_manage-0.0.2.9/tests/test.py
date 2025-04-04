import warnings
from unittest import TestCase

from parade_manage.common.node import Node

from parade_manage.common.dag import DAG

from parade_manage import ParadeManage
from parade_manage.utils import walk_modules, tree, show_check_info


class Test(TestCase):

    def setUp(self) -> None:
        warnings.filterwarnings("ignore", category=DeprecationWarning)

        tasks = {
            "g": [], "h": [], "d": ["g"],
            "e": ["g", "h"], "a": ["d", "e"],
            "b": ["e", "f"], "c": ["f"],
            "k": [], "f": []
        }
        self.tasks = {Node(k, k): [Node(v, v) for v in vs] for k, vs in tasks.items()}
        self.dag = DAG.from_graph(self.tasks)

    def test_circular_dag(self):
        tasks = {
            "g": ["a"], "a": ["g"]
        }
        nodes = {Node(k, k): [Node(v, v) for v in vs] for k, vs in tasks.items()}
        DAG.from_graph(nodes)

    def test_check(self):
        tasks = {
            "g": ["a"], "a": ["g"], "b": ["b", "h"],
            "c": [], "k": [], "d": ["k", "c", "k"],
            "k1": ["k3"], "k2": ["k1"], "k3": ["k2"]
        }
        show_check_info(tasks)

    def test_check_normal(self):
        tasks = {
            "a": [], "b": [], "c": [],
            "k": ["a", "b"]
        }
        show_check_info(tasks)

    def test_walk_modules(self):
        print(walk_modules("../parade_manage/common"))

    def test_dump(self):
        pass

    def test_tree(self):

        tasks = {"flow-1": ["a", "b", "c"], "a": []}

        tree(tasks, "flow-1")

    def test_leaf_nodes(self):
        self.assertCountEqual([n.name for n in self.dag.leaf_nodes], ["g", "h", "f", "k"])

    def test_root_nodes(self):
        self.assertCountEqual([n.name for n in self.dag.root_nodes], ["a", "b", "c", "k"])

    def test_isolated_nodes(self):
        self.assertCountEqual([n.name for n in self.dag.isolated_nodes], ["k"])

    def test_show_tree(self):
        m = ParadeManage("/path/to/project")
        m.tree(flow_name="test-tree")

    def test_show_table(self):
        m = ParadeManage("/path/to/project")
        m.show()

    def test_sort(self):
        a = Node("A", "A")
        b = Node("B", "B", 2)
        c = Node("C", "C", 6)
        d = Node("D", "D", 3)
        e = Node("E", "E")
        f = Node("F", "F", 8)

        dag = DAG()
        dag.add_node(a)
        dag.add_node(b)
        dag.add_node(c)
        dag.add_node(d)
        dag.add_node(e)
        dag.add_node(f)

        dag.add_edge(c, a)
        dag.add_edge(c, b)
        dag.add_edge(e, c)
        dag.add_edge(e, d)
        dag.add_edge(f, a)
        dag.add_edge(f, b)

        sorted_nodes = dag.list()
        self.assertCountEqual([n.name for n in sorted_nodes], ["D", "B", "A", "F", "C", "E"])
