from django.shortcuts import render
from post.models import Post,Status,Category

def politics_view(request):
    politics  = Post.objects.filter(status=Status.PUBLISH,category=Category.objects.get(category='rajniti')).order_by('-created_at')
    print(politics) 
    context = {"politics":politics}
    return render(request,"politics.html",context)
