from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.

class HomeData(models.Model):
    title = models.CharField(max_length=250)
    about = RichTextUploadingField()
    mission = RichTextUploadingField()
    quote = RichTextUploadingField()
    sub_industries = RichTextUploadingField()

    def __str__(self):
        return self.title
    

class Slider(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='slider')
    home_data = models.ForeignKey(HomeData, null=True, on_delete=models.SET_NULL, related_name='sliders')

    def __str__(self):
        return self.title
    

class Features(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True)
    home_data = models.ForeignKey(HomeData, null=True, on_delete=models.SET_NULL, related_name='features')

    def __str__(self):
        return self.title


class SiteInformation(models.Model):
    title = models.CharField(max_length=200)
    logo_light = models.ImageField(upload_to='logo', null=True)
    logo_dark = models.ImageField(upload_to='logo', null=True)
    description = models.TextField(null=True)
    phone = models.CharField(max_length=11, null=True)
    address = models.CharField(max_length=300, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.title
    

class SocialLinks(models.Model):
    label = models.CharField(max_length=120, null=True)
    icon = models.CharField(null=True, max_length=200)
    link = models.CharField(max_length=200,blank=True,null=True)
    main_data = models.ForeignKey(SiteInformation, null=True, on_delete=models.SET_NULL, related_name='socials')

    def __str__(self):
        return self.label
