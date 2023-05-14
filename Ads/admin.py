from django.contrib import admin
from Ads.models import AdCategory, Ads
from django.utils.html import format_html

@admin.register(AdCategory)
class AdCategoryAdmin(admin.ModelAdmin):
    list_display = ("ads_category","created_at","modified_at",)
    search_fields = ("ads_category",)

@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_per_page = 10

    def image_tag(self, obj):
        return format_html('<img src="{}" width="250" height="200" />'.format(obj.image.url))
    

    image_tag.short_description = 'Image'

    
    list_display = ("image_tag","name","ads_category")
    search_fields = ("name","ads_category")    
