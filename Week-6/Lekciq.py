class Comment:
    def __init__(self, username, content, likes= 0 ):
        self.username = username
        self.content = content
        self.likes = likes

comment = Comment(input(), input(), input(), )
print(comment.username)
print(comment.content)
print(comment.likes)