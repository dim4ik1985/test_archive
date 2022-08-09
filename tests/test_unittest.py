import unittest
from main import ArchiveOfDocuments
from parameterized import parameterized


class TestFunction(unittest.TestCase):

    def setUp(self):
        self.instance = ArchiveOfDocuments()

    @parameterized.expand(
        [
            ("2207 876234", "Василий Гупкин"),
            ("11-2", "Геннадий Покемонов")
        ]
    )
    def test_cls_get_search_name_on_doc(self, num_doc, result):
        """Тест поиска имени по номеру документа"""
        calc_result = self.instance.get_search_name_on_doc(num_doc)
        self.assertEqual(calc_result, result)

    def test_cls_get_search_shelf_on_doc(self):
        """Тест поиска номера полки по номеру документа"""
        result = self.instance.get_search_shelf_on_doc('11-2')
        etalon = '1'
        self.assertEqual(result, etalon)

    def test_cls_get_add_shelf(self):
        """Тест функции добавления полки"""
        result = self.instance.get_add_shelf(3)
        self.assertTrue(result)

    def test_cls_get_del_doc(self):
        """Тест удаления документа"""
        result = self.instance.get_del_doc('10006')
        self.assertTrue(result)
