from django.contrib import admin
from post.models import Category,Post,Tag 

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category","created_at","modified_at",)
    search_fields = ("category",)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("tags","created_at","modified_at",)
    search_fields = ("tags",)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title","Subtitle","summary","dateline","category","tags","reporter","content","created_at","modified_at",)
    search_fields = ("title",)    

