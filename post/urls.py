from django.urls import path
from post.views import politics_view
app_name = "post"
urlpatterns = [
    path('politics',politics_view,name="politics"),
]
