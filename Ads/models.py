
from django.db import models
from django.utils.html import escape

# Create your models here.


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


class AdCategory(TimeStampModel):
    ads_category = models.CharField(max_length=250,verbose_name="category")

    def __str__(self):
        return self.ads_category
    

    class Meta:
        verbose_name_plural = "categories"
    

class Ads(TimeStampModel):
    ads_category = models.ForeignKey(AdCategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to="ads_images/",blank=False,unique=True)

    def _str_(self):
        return self.name
    

    class Meta:
        verbose_name = "Ad"
        verbose_name_plural = "Ads"
    
    
    
    def image_tag(self):
        return u'<img src="%s" />' % escape("post/images")
    
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True