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


    context = {"posts": posts,"politics":politics,"news":news,"laws":laws,"sports":sports,"education":education,"main_content":main_content}
    return render(request,"index.html",context)



def about_view(request):
    return render(request,"about.html")


def get_latest_func():
    from post.views import func_post
    return func_post()



def advertisement_view(request):
    latest_func = get_latest_func()

    return render(request,"advertisement.html",{"posts":latest_func})




def contact_view(request):
    latest_func = get_latest_func()

    return render(request,"contact.html",{"posts":latest_func})


