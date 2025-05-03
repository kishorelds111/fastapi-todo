import unittest
import os
from todo import TodoApp

class TestTodoApp(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_tasks.txt"
        self.app = TodoApp(filename=self.test_file)

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_task(self):
        self.app.add_task("Learn Python")
        self.assertIn("Learn Python", self.app.view_tasks())

    def test_delete_task(self):
        self.app.add_task("Test Delete")
        deleted = self.app.delete_task(0)
        self.assertEqual(deleted, "Test Delete")
        self.assertNotIn("Test Delete", self.app.view_tasks())

    def test_load_tasks(self):
        self.app.add_task("Save Test")
        new_app = TodoApp(filename=self.test_file)
        self.assertIn("Save Test", new_app.view_tasks())

if __name__ == "__main__":
    unittest.main()
