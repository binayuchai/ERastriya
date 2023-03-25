from django.db import models
from useraccount.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
from django.utils.html import escape
import hashlib
from django.core.files.storage import FileSystemStorage


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


    class Meta:
        abstract = True


class Category(TimeStampModel):
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.category


class Tag(TimeStampModel):
    tags = models.CharField(max_length=250)

    def __str__(self):
        return self.tags


class Status(models.TextChoices):
    DRAFT = "draft", "DRAFT"
    PUBLISH = "publish", "PUBLISH"
    BLOCKED = "blocked", "BLOCKED"
    

# def md5_checksum(file):
#     with file.open('rb') as f:
#         checksum = hashlib.md5(f.read()).hexdigest()
#     return checksum


# def unique_upload_to(instance, filename):
#     if not instance.image:
#         return filename
    
#     storage = FileSystemStorage()
#     checksum = md5_checksum(instance.image)
#     existing_files = storage.listdir('post/images')[1]
#     for name in existing_files:
#         with storage.open(f'post/images/{name}') as f:
#             if md5_checksum(f) == checksum:
#                 return name
#     return filename
            

class Post(TimeStampModel):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag,on_delete=models.CASCADE)
    reporter = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    Subtitle = models.CharField(max_length=250,blank=True,null=True)
    summary = models.TextField()
    content = RichTextUploadingField(blank=True,null=True)
    dateline = models.DateField()
    image = models.ImageField(upload_to="post/images",blank=True,null=True)
    status = models.CharField(max_length=50,choices=Status.choices,default=Status.DRAFT)


    def __str__(self):
        return self.title


    def image_tag(self):
        return u'<img src="%s" />' % escape("post/images")
    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
       

    
