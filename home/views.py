from django.shortcuts import render
from post.models import Category,Status,Post

def home_page(request):
    posts = Post.objects.filter(status=Status.PUBLISH).order_by('-created_at')
    politics  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='politics')).order_by('-created_at')[:4]
    news  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='news')).order_by('-created_at')[:4]
    big_news = news[3]        
    print(big_news)

    context = {"posts": posts,"politics":politics,"news":news,"big_news":big_news}
    return render(request,"index.html",context)

