from unittest import TestCase
from blog.blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test Title', 'Test Author')
        self.assertEqual('Test Title', b.title)
        self.assertEqual('Test Author', b.author)
        self.assertListEqual([], b.posts)
    
    def test_repr(self):
        b = Blog('Test Title', 'Test Author')
        self.assertEqual('Test Title by Test Author (0 posts)', b.__repr__())
        b.create_post('Test Post', 'Test Content')
        self.assertEqual('Test Title by Test Author (1 post)', b.__repr__())
        b.create_post('Another Test Post', 'Another Test Content')
        self.assertEqual('Test Title by Test Author (2 posts)', b.__repr__())
    
    def test_create_post(self):
        b = Blog('Test Title', 'Test Author')
        b.create_post('Test Post', 'Test Content')
        self.assertListEqual([{'title': 'Test Post', 'content': 'Test Content'}], b.posts)
        self.assertEqual('Test Post', b.posts[0]['title'])
        self.assertEqual('Test Content', b.posts[0]['content'])
    
    def test_json(self):
        b = Blog('Test Title', 'Test Author')
        self.assertDictEqual({
            'title': 'Test Title',
            'author': 'Test Author',
            'posts': [],
        }, b.json())
        b.create_post('Test Post', 'Test Content')
        self.assertDictEqual({
            'title': 'Test Title',
            'author': 'Test Author',
            'posts': [{'title': 'Test Post', 'content': 'Test Content'}]
        }, b.json())