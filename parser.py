import json

with open('./temp/maaslalani.json') as f:
    posts = json.load(f)

comments_to_likes_ratio = []

for post in posts:
    comments_to_likes_ratio.append(post['edge_media_to_comment']['count'] / post['edge_media_preview_like']['count'])

print(comments_to_likes_ratio)
