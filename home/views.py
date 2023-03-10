from django.shortcuts import render
from post.models import Category,Status,Post

def home_page(request):
    posts = Post.objects.filter(status=Status.PUBLISH)
    politics  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='politics')).order_by('-created_at')[:4]

    context = {"posts": posts,"politics":politics}
    return render(request,"index.html",context)

