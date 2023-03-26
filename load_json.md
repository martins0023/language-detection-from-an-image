import json
from

with open('posts.json') as f:
    posts_json = json.load(f)
    
 for post in posts_json:
     post = Post(text=post['text'])
     post.save()
