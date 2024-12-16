from unittest import TestCase
from blog.blog import Blog
from blog.post import Post


class BlogTest(TestCase):
    def test_create_post(self):
        b = Blog('Test Title', 'Test Author')
        b.create_post('Test Post', 'Test Content')
        self.assertEqual(1, len(b.posts))
        self.assertEqual('Test Post', b.posts[0].title)
        self.assertEqual('Test Content', b.posts[0].content)


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
            'posts': [{'title': 'Test Post',
                        'content': 'Test Content'}],
        }, b.json())
        