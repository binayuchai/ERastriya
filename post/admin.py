from django.contrib import admin
from post.models import Category,Post,Tag 
from django.utils.html import format_html

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
    # def image_tag(self, obj):
    #     return format_html('<img src="{}" width="250" height="200" />'.format(obj.image.url))
    
    # image_tag.short_description = 'Image'

    
    list_display = ("title","Subtitle","summary","dateline","category","tags","reporter","created_at","modified_at",)
    search_fields = ("title",)    

