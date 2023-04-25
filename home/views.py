from django.shortcuts import render
from post.models import Category,Status,Post
from post.utils import get_or_none

def home_page(request):
    posts = Post.objects.filter(status=Status.PUBLISH).order_by('-created_at')
    politics  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='politics')).order_by('-created_at')[:5]
    news  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='news')).order_by('-created_at')[:4]
    laws  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='laws')).order_by('-created_at')[:5]

    # big_news = get_or_none( Post,Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='news'))[3:4])
    # print(big_news)
    # big_politics = get_or_none( Post,Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='politics'))[4:5])
    # big_laws = get_or_none( Post,Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='laws'))[4:5])
    # if big_news is None:
    #     big_news = None

    # if big_politics is None:
    #     big_politics = None
    
    # if big_laws is None:
    #     big_laws = None
    
        
    
    print(news)
    
    print(laws)
    context = {"posts": posts,"politics":politics,"news":news,"laws":laws}#"big_news":big_news,"big_politics":big_politics,"laws":laws,"big_laws":big_laws}
    return render(request,"index.html",context)

