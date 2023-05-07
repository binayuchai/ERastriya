from django.urls import path
from post.views import politics_view, news_view, law_view, sports_view, education_view, detail_view, search_result, other_view
app_name = "post"
urlpatterns = [
    path('politics',politics_view,name="politics"),
    path('news',news_view,name="news"),
    path('law',law_view,name="law"),
    path('sports',sports_view,name="sports"),
    path('education',education_view,name="education"),
    path('post-detail/<int:postid>/',detail_view,name="detail"),
    path('search/',search_result,name="search_result"),
    path('others',other_view,name="others"),

    
]