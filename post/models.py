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
from bs4 import BeautifulSoup


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
   
    def save(self, *args, **kwargs):

        # Convert the CKEditor content to BeautifulSoup object
        soup = BeautifulSoup(self.content, 'html.parser')
       # Find all <img> tags in the CKEditor content
        img_tags = soup.find_all('img')


        for img_tag in img_tags:
            # Get the image URL from the <img> tag
            img_s = img_tag.get('src', '')
            src = img_s            

            if src:
                # Open the image from the URL
                response = requests.get(src)
                image = Image.open(BytesIO(response.content))

                # Resize the image
                min_size = (200, 200)
                image.thumbnail(min_size)

                # Save the resized image to a byte stream
                resized_image_bytes = BytesIO()
                image.save(resized_image_bytes, format='JPEG')
                resized_image_bytes.seek(0)

                # Update the <img> tag with the resized image data
                img_tag.attrs['src'] = src
                img_tag.attrs['data-image-original'] = src
                img_tag.attrs['data-image-thumbnail'] = resized_image_bytes

        # Convert the modified BeautifulSoup object back to HTML string
        self.content = str(soup)
        super().save(*args, **kwargs)




    
