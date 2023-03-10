from django.db import models
from useraccount.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget
from django.utils.html import escape


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
    
    
class Post(TimeStampModel):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ForeignKey(Tag,on_delete=models.CASCADE)
    reporter = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    Subtitle = models.CharField(max_length=250,blank=True,null=True)
    summary = models.TextField()
    content = RichTextUploadingField(blank=True,null=True)
    dateline = models.DateField()
    featured_image = models.ImageField(upload_to="post/images",blank=True,null=True)
    status = models.CharField(max_length=50,choices=Status.choices,default=Status.DRAFT)


    def __str__(self):
        return self.title


    # def image_tag(self):
    #     return u'<img src="%s" />' % escape("post/images")
    # image_tag.short_description = 'Image'
    # image_tag.allow_tags = True
       

    
