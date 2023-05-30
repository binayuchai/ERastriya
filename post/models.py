from django.conf import settings
from django.db import models
from django.forms import ValidationError
from erastriya.settings import MEDIA_ROOT
from useraccount.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.html import escape
from django.urls import reverse
from PIL import Image
import io
import imagehash
from django.core.files.uploadedfile import SimpleUploadedFile
from io import BytesIO
import os
from embed_video.fields import EmbedVideoField
import requests
import re

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


class Category(TimeStampModel):
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.category
    

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Tag(TimeStampModel):
    tags = models.CharField(max_length=250)

    def __str__(self):
        return self.tags


class Status(models.TextChoices):
    DRAFT = "draft", "DRAFT"
    PUBLISH = "publish", "PUBLISH"
    BLOCKED = "blocked", "BLOCKED"
    
class Home_content(models.TextChoices):
    YES = "yes", "YES"
    NO = "no", "NO"


          

class Post(TimeStampModel):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag,on_delete=models.CASCADE)
    reporter = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    Subtitle = models.CharField(max_length=250,blank=True,null=True)
    summary = models.TextField()
    content = RichTextUploadingField(blank=True,null=True)
    dateline = models.DateField()
    image = models.ImageField(upload_to="images/",blank=True,null=True,unique=True)
    home_content = models.CharField(max_length=50,choices=Home_content.choices,default=Home_content.NO,blank=True,null=True)
    video = EmbedVideoField(blank=True,null=True)  # same like models.URLField()
    status = models.CharField(max_length=50,choices=Status.choices,default=Status.DRAFT)
    image_hash = models.CharField(max_length=64, blank=True)



    def __str__(self):
        return self.title

    
    def image_tag(self):
        return u'<img src="%s" />' % escape("post/images")
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'pk': self.pk})

    #compress the image 

    # def save(self, *args, **kwargs):
    #    instance = super(Post, self).save(*args, **kwargs)
    #    image = Image.open(self.image.path)
    #    image.save(self.image.path,quality=60,optimize=True)
    #    return instance

    def save(self, *args, **kwargs):
        super(Post,self).save(*args, **kwargs)

        #Compress CKEditor image
        self.compress_ckeditor_images()

        #Compress normal image
        self.compress_normal_image()


    def compress_ckeditor_images(self):

        # Finding the image from ckeditor
        if self.content:
            # Regular expression to match CKEditor image tags
            pattern = r'<img[^>]+src="([^">]+)"[^>]*>'

            image_tags = re.findall(pattern,self.content)

            for image_url in image_tags:
                image_path = self.get_image_path(image_url)
                if image_path:
                    self.compress_image(image_path)


    def compress_normal_image(self):
        #Compress the normal image
        if self.image:
            image_path = self.image.path
            self.compress_image(image_path)

    def get_image_path(self,image_url):
         #Remove the protocol and domain from the image URL
        # to get the relative path
        relative_path = image_url.replace(settings.MEDIA_URL, "")

        # Join the relative path with the base media root to get the full file path
        full_path = os.path.join(settings.MEDIA_ROOT, relative_path)
        return full_path
    
    def compress_image(self,image_path):
        image = Image.open(image_path)
        image.save(image_path,quality=60,optimize=True)

        



            




    
