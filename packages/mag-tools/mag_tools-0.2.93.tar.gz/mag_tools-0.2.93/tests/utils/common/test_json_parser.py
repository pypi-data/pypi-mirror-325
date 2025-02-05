import unittest
from datetime import datetime
from anytree import RenderTree

from mag_tools.utils.common.json_parser import JsonParser


class TestJsonParser(unittest.TestCase):

    def test_to_string(self):
        json_str = '"Hello,World!"'
        result = JsonParser.to_string(json_str)
        self.assertEqual(result, "Hello,World!")

    def test_to_decimal(self):
        decimal_str = '123.45'
        result = JsonParser.to_decimal(decimal_str)
        self.assertEqual(result, 123.45)

    def test_to_float(self):
        float_str = '123.45'
        result = JsonParser.to_float(float_str)
        self.assertEqual(result, 123.45)

    def test_to_int(self):
        int_str = '123'
        result = JsonParser.to_int(int_str)
        self.assertEqual(result, 123)

    def test_to_datetime(self):
        datetime_str = '"2023-04-06T11:54:03.000Z"'
        result = JsonParser.to_datetime(datetime_str)
        self.assertEqual(result, datetime.strptime("2023-04-06T11:54:03.000Z", '%Y-%m-%dT%H:%M:%S.%fZ'))

    def test_to_bool(self):
        bool_str = '"true"'
        result = JsonParser.to_bool(bool_str)
        self.assertTrue(result)

    def test_to_list(self):
        list_str = '[{"name":"John"}, {"name":"Jane"}]'
        result = JsonParser.to_list(list_str, dict)
        self.assertEqual(result, [{'name':'John'}, {'name':'Jane'}])

    def test_to_map(self):
        map_str = '{"key1": "value1", "key2": "value2"}'
        result = JsonParser.to_map(map_str, str, str)
        self.assertEqual(result, {"key1": "value1", "key2": "value2"})

    def test_to_tree(self):
        tree_str = '{"name": "root", "children": [{"name": "child1"}, {"name": "child2"}]}'
        result = JsonParser.to_tree(tree_str, str)
        self.assertEqual(result.name, "root")
        self.assertEqual(len(result.children), 2)
        self.assertEqual(result.children[0].name, "child1")
        self.assertEqual(result.children[1].name, "child2")

        # 打印树结构
        for pre, fill, node in RenderTree(result):
            print("%s%s" % (pre, node.name))

if __name__ == '__main__':
    unittest.main()
