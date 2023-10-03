from lib.post import Post

def test_initialised_properly():
    post = Post(1, 'My first post', 'Hello world!', 0, 1)

    assert post.id == 1
    assert post.title == 'My first post'
    assert post.content == 'Hello world!'
    assert post.views == 0
    assert post.account_id == 1

def test_repr():
    post = Post(1, 'My first post', 'Hello world!', 0, 1)
    assert str(post) == "Post(1, My first post, Hello world!, 0, 1)"

def test_eq():
    post_1 = Post(1, 'My first post', 'Hello world!', 0, 1)
    post_2 = Post(1, 'My first post', 'Hello world!', 0, 1)
    assert post_1 == post_2