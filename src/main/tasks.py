from domru.celery import app
from .models import Post
from datetime import datetime



@app.task #регистриуем таску
def repeat_order_make():
    post = Post.objects.create(title=f"Post - {datetime.now()}")
    print(f"{post.title} -- Post created")
    return "необязательная заглушка"