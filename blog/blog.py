class Blog:
    def __init__(self, title, author):
        self.posts = []
        self.title = title
        self.author = author
    
    def __repr__(self):
        return f'{self.title} by {self.author} ({len(self.posts)} post{"s" if len(self.posts) != 1 else ""})'

    def create_post(self, title, content):
        self.posts.append({'title': title, 'content': content})
    
    def json(self):
        return {
            'title': self.title,
            'author': self.author,
            'posts': self.posts
        }