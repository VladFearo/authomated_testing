from unittest import TestCase
from blog.post import Post  # Adjust the import to reflect the package structure

class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test Content')
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)

    def test_json(self):
        p = Post('Test', 'Test Content')
        expected = {'title': 'Test', 'content': 'Test Content'}
        self.assertDictEqual(expected, p.json())

    def test_repr(self):
        p = Post('Test', 'Test Content')
        self.assertEqual('<Post Test>', p.__repr__())