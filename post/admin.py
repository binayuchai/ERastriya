from django.contrib import admin
from post.models import Category,Post,Tag 
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode
from imagekit.admin import AdminThumbnail
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
    list_per_page = 10
    def image_tag(self, obj):
        return format_html('<img src="{}" width="250" height="200" />'.format(obj.image.url))
    
    def view_post(self, obj):
        url = reverse('post:detail', args=[obj.pk])
        return format_html("<a href='{}'>{}</a>", url, "visit")
    view_post.short_description = 'Post Link'
    
    view_post.short_description = 'View'
    

    image_tag.short_description = 'Image'

    
    list_display = ("image_tag","title","dateline","category","tags","reporter","view_post",)
    search_fields = ("title",)    



