from django.shortcuts import render,get_object_or_404
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
    context = {"politics":politics,"posts":posts,"page_obj":page_obj,"additional_range":range(7,13),"pagination_range":page_obj.paginator.get_elided_page_range(on_each_side=5, on_ends=2)}
    return render(request,"politics.html",context)


def news_view(request):
    posts = func_post()
    news  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='news')).order_by('-created_at')
    page_obj = lisiting(request,news)
    context = {"news":news,"posts":posts,"page_obj":page_obj}
    return render(request,"news.html",context)



def education_view(request):
    posts = func_post()
    educations  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='education')).order_by('-created_at')    
    page_obj = lisiting(request,educations)
    education  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='education')).order_by('-created_at')
    context = {"education":education,"posts":posts,"page_obj":page_obj,"pagination_range":page_obj.paginator.get_elided_page_range(on_each_side=5, on_ends=2)}
    return render(request,"education.html",context)



def sports_view(request):
    posts = func_post()
    sports  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='sports')).order_by('-created_at')
    page_obj = lisiting(request,sports)

    context = {"sports":sports,"posts":posts,"page_obj":page_obj}
    return render(request,"sports.html",context)



def law_view(request):
    posts = func_post()
    laws  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='laws')).order_by('-created_at')
    page_obj = lisiting(request,laws)
    context = {"laws":laws,"posts":posts,"page_obj":page_obj}
    return render(request,"law.html",context)


def other_view(request):
    posts = func_post()
    others  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='others')).order_by('-created_at')
    page_obj = lisiting(request,others)
    context = {"others":others,"posts":posts,"page_obj":page_obj}
    return render(request,"others.html",context)



def detail_view(request,postid):
    posts = func_post()
    post_item = get_object_or_404(Post, id=postid)
    post_category = post_item.category
    additional_news  = list(Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category=post_category)).order_by('-created_at')[:5])
    if post_item in additional_news:
        additional_news.remove(post_item)

        
    soup = BeautifulSoup(post_item.content, 'html.parser')
    images = soup.find_all('img')
    image_list =''
    for img in images:
        src = img.get('src', '')
        image_list = src

    desc = soup.get_text()

    context = {"post":post_item,"posts":posts,"images":image_list,"description":desc,"current_url": request.build_absolute_uri(),"additional_news":additional_news}
    return render(request,"post_detail.html",context)


def search_result(request):
    posts = func_post()
    record_found = True
    query = "No Result Found"
    result = None
    context = {}

    if 'q' in request.GET:
        query = request.GET.get('q')
        print(query)
        result  = Post.objects.filter(status=Status.PUBLISH,title__icontains=query).order_by('-created_at')
        if result:
            page_obj = lisiting(request,result)
        else:
            record_found = False
        print(record_found)
        if record_found:
            context = {"posts":posts,"results":result,"record_found":record_found,"query":query,"page_obj":page_obj,"pagination_range":page_obj.paginator.get_elided_page_range(on_each_side=5, on_ends=2)}
        else:
            context = {"posts":posts,"results":result,"record_found":record_found,"query":query}
    return render(request,"searched_result.html",context)
