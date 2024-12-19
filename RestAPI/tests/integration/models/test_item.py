from RestAPI.models.item import ItemModel
from RestAPI.tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            item = ItemModel('test', 19.99)

            self.assertIsNone(ItemModel.find_by_name('test'),
                            "Found an item with name 'test' before save_to_db")

            item.save_to_db()

            self.assertIsNotNone(ItemModel.find_by_name('test'),
                                "Item not found in database.")

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('test'),
                            "Found an item with name 'test' after delete_from_db")
        
