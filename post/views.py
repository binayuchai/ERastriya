from django.shortcuts import render
from post.models import Post,Status,Category
from bs4 import BeautifulSoup
from django.core.paginator import Paginator

def func_post():
    posts = Post.objects.filter(status=Status.PUBLISH).order_by('-created_at')[:8]
    return posts

def lisiting(request,category_list):
    category_wise_list = category_list
    paginator = Paginator(category_wise_list,12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj





def politics_view(request):
    posts = func_post()
    politics  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='politics')).order_by('-created_at')
    page_obj = lisiting(request,politics)
    print(type(page_obj))

    context = {"politics":politics,"posts":posts,"page_obj":page_obj,"additional_range":range(7,13)}
    return render(request,"politics.html",context)


def news_view(request):
    posts = func_post()
    news  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='news')).order_by('-created_at')
    context = {"news":news,"posts":posts}
    return render(request,"news.html",context)



def education_view(request):
    posts = func_post()
    education  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='education')).order_by('-created_at')
    context = {"education":education,"posts":posts}
    return render(request,"education.html",context)



def sports_view(request):
    posts = func_post()
    sports  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='sports')).order_by('-created_at')
    context = {"sports":sports,"posts":posts}
    return render(request,"sports.html",context)



def law_view(request):
    posts = func_post()
    laws  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='laws')).order_by('-created_at')
    context = {"laws":laws,"posts":posts}
    return render(request,"law.html",context)



def detail_view(request,postid):
    post = Post.objects.get(id=postid)
    soup = BeautifulSoup(post.content, 'html.parser')
    images = soup.find_all('img')
    image_list =''
    for img in images:
        src = img.get('src', '')
        image_list = src

    desc = soup.get_text()
    context = {"post":post,"images":image_list,"description":desc}
    return render(request,"post_detail.html",context)


