from django.shortcuts import render
from post.models import Category,Status,Post
def home_page(request):
    post = Post.objects.filter(status=Status.PUBLISH)
    politics  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='rajniti')).order_by('-created_at')

    context = {"posts": post,"politics":politics}
    return render(request,"index.html",context)