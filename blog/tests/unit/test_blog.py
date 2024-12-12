from unittest import TestCase
from blog.blog import Blog
from blog.post import Post

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
    
    