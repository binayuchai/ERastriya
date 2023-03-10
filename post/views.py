from django.shortcuts import render
from post.models import Post,Status,Category
from bs4 import BeautifulSoup


def politics_view(request):
    politics  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='politics')).order_by('-created_at')
    context = {"politics":politics}
    return render(request,"politics.html",context)


def news_view(request):
    news  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='news')).order_by('-created_at')
    context = {"news":news}
    return render(request,"news.html",context)



def education_view(request):
    education  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='education')).order_by('-created_at')
    context = {"education":education}
    return render(request,"education.html",context)



def sports_view(request):
    sports  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='sports')).order_by('-created_at')
    context = {"sports":sports}
    return render(request,"sports.html",context)



def law_view(request):
    laws  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='laws')).order_by('-created_at')
    context = {"laws":laws}
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
