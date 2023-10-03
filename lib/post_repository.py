from lib.post import *

class PostRepository():
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM posts')
        posts = []

        for row in rows:
            posts.append(Post(row['id'], row['title'], row['content'], row['views'], row['account_id']))

        return posts

    def find(self, id):
        row = self._connection.execute(f"SELECT * FROM posts WHERE id = {id}")[0]

        return Post(row['id'], row['title'], row['content'], row['views'], row['account_id'])

    def find_account_posts(self, account_id):
        rows = self._connection.execute(f"SELECT * FROM posts WHERE account_id = {account_id}")
        posts = []

        for row in rows:
            posts.append(Post(row['id'], row['title'], row['content'], row['views'], row['account_id']))

        return posts

    def create_post(self, title, content, account_id):
        query = f"INSERT INTO posts (title, content, views, account_id) VALUES ('{title}', '{content}', 0, {account_id})"
        self._connection.execute(query)
