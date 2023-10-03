from lib.post_repository import *

def test_all_posts(db_connection):
    db_connection.seed('seeds/social_network.sql')
    post_repo = PostRepository(db_connection)

    posts = post_repo.all()

    assert len(posts) == 3

def test_find_post(db_connection):
    db_connection.seed('seeds/social_network.sql')
    post_repo = PostRepository(db_connection)

    post = post_repo.find(1)

    assert post.id == 1
    assert post.title == 'My first post'
    assert post.content == 'This is my first post'

def test_find_account_posts(db_connection):
    db_connection.seed('seeds/social_network.sql')
    post_repo = PostRepository(db_connection)

    posts = post_repo.find_account_posts(1)

    assert len(posts) == 2
    assert posts[0].title == 'My first post'
    assert posts[1].title == 'My second post'

def test_create_post(db_connection):
    db_connection.seed('seeds/social_network.sql')
    post_repo = PostRepository(db_connection)

    post_repo.create_post('My third post', 'Hello third world!', 1)

    assert len(post_repo.all()) == 4