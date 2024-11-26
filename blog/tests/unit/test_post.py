from unittest import TestCase
from blog.post import Post  # Adjust the import to reflect the package structure

class PostTest(TestCase):
    def test_create_post(self):
        p = Post('Test', 'Test Content')
        self.assertEqual('Test', p.title)
        self.assertEqual('Test Content', p.content)