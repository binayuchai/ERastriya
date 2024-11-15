from django.urls import path
from home.views import home_page,about_view,contact_view,advertisement_view
app_name = "home"
urlpatterns = [
    path('',home_page,name="home_page"),
    path('about/',about_view,name="about"),
    path('contact/',contact_view,name="contact"),
    path('advertisement-info/',advertisement_view,name="advertisement_info"),
]
