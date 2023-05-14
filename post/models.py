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

    
    # def get_image_hash(self):
    #     with open(os.path.join(MEDIA_ROOT, self.image.name), 'rb') as f:
    #         image_bytes = f.read()
    #         image_hash = str(imagehash.average_hash(Image.open(BytesIO(image_bytes))))
    #     return image_hash



    # def save(self, *args, **kwargs):
    #      # Check if the image already exists in the database
    #     if self.pk is None:
    #         image_hash = self.get_image_hash()
    #         if Post.objects.filter(image_hash=image_hash).exists():
    #             return
    #         self.image_hash = image_hash
    #         print(image_hash)
    #     super().save(*args, **kwargs)




    # def get_absolute_url(self):
    #     return reverse('detail_view', args=[str(self.id)])

    # def save(self, *args, **kwargs):
    #     # Check if the image file already exists in the database
    #     file_hash = hashlib.md5(self.image_file.read()).hexdigest()
    #     if Post.objects.filter(file_hash=file_hash).exists():
    #         raise ValueError('Image already exists.')
    #     self.file_hash = file_hash
    #     super(Post,self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #         # generate hash of the image content
    #         image_hash = hashlib.md5(self.image.read()).hexdigest()

    #         # set file name to hash + extension of the uploaded file
    #         file_name = f"{image_hash}.{self.image.name.split('.')[-1]}"

    #         # save image with the new file name
    #         self.image.save(file_name, ContentFile(self.image.read()), save=False)

    #         super().save(*args, **kwargs)
    # def save(self, *args, **kwargs):
    #         # find all images in the content_with_images field
    #     images = self.image.images

    #     # loop through images and replace the file name with hash of content
    #     for image in images:
    #         image_hash = hashlib.md5(image.file.read()).hexdigest()
    #         image.name = f"{image_hash}.{image.name.split('.')[-1]}"
    #         # save image with the new file name
    #         image.file.save(image.name, ContentFile(image.file.read()), save=False)

    #     super().save(*args, **kwargs)
    
    # def save(self, *args, **kwargs):
    # # find all images in the content_with_images field
    #     images = self.image

    #     # loop through images and set the upload_to parameter to images/
    #     for image in images:
    #         # compute the perceptual hash of the image content
    #         image_content = image.read()
    #         image_hash = str(imagehash.phash(Image.open(io.BytesIO(image_content))))
            
    #         # check if the image has already been uploaded
    #         qs = Post.objects.filter(image_hash=image_hash)
    #         if qs.exists():
    #             # use the existing image instead of the uploaded one
    #             self.content_with_images = self.content_with_images.replace(
    #                 str(image), str(qs.first().content_with_images.url))
    #         else:
    #             # save the uploaded image and update its hash
    #             image_name = self.upload_to(image.name)
    #             image_file = SimpleUploadedFile(image_name, image_content)
    #             self.content_with_images = self.content_with_images.replace(str(image), image_name)
    #             self.image_hash = image_hash
    #             self.content_with_images.storage.save(image_name, image_file)
    #     super().save(*args, **kwargs)





    
