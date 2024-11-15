from django.urls import path
from post.views import (
    politics_view, news_view, law_view, sports_view, 
    education_view, detail_view, search_result,
    other_view, international_view, business_view,
    scienceandtech_view, entertainment_view, economy_view, 
    literature_view, religion_culture_view, capital_market_view
    
)

app_name = "post"
urlpatterns = [
    path('politics/',politics_view,name="politics"),
    path('news/',news_view,name="news"),
    path('law/',law_view,name="law"),
    path('sports/',sports_view,name="sports"),
    path('education/',education_view,name="education"),
    path('international/',international_view,name="international"),
    path('business/',business_view,name="business"),
    path('economy/',economy_view,name="economy"),
    path('entertainment/',entertainment_view,name="entertainment"),
    path('science-technology/',scienceandtech_view,name="scienceandtech"),
    path('literature/',literature_view,name="literature"),
    path('religion-culture/',religion_culture_view,name="religion_culture"),
    path('capital-market/',capital_market_view,name="capital_market"),
    path('post-detail/<int:id>/',detail_view,name="detail"),
    path('search/',search_result,name="search_result"),

    
]