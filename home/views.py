from django.shortcuts import render
from post.models import Category,Status,Post,Home_content
from post.utils import get_or_none

def home_page(request):
    posts = Post.objects.filter(status=Status.PUBLISH).order_by('-created_at')
    main_content = Post.objects.filter(status=Status.PUBLISH,home_content=Home_content.YES).order_by('-created_at')[:1]
    print(main_content)
    politics  = Post.objects.filter(status=Status.PUBLISH,home_content=Home_content.NO,category=Category.objects.get(category='politics')).order_by('-created_at')[:6]
    news  = Post.objects.filter(status=Status.PUBLISH,home_content=Home_content.NO,category=Category.objects.get(category='news')).order_by('-created_at')[:6]
    laws  = Post.objects.filter(status=Status.PUBLISH,home_content=Home_content.NO,category=Category.objects.get(category='laws')).order_by('-created_at')[:6]
    sports  = Post.objects.filter(status=Status.PUBLISH,home_content=Home_content.NO,category=Category.objects.get(category='sports')).order_by('-created_at')[:6]
    education  = Post.objects.filter(status=Status.PUBLISH,home_content=Home_content.NO,category=Category.objects.get(category='education')).order_by('-created_at')[:6]


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
    
        
    
    # print(news)
    
    # print(laws)
    context = {"posts": posts,"politics":politics,"news":news,"laws":laws,"sports":sports,"education":education,"main_content":main_content}
    return render(request,"index.html",context)

