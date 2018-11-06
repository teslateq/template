from django.db import models
from colorfield.fields import ColorField

class Project(models.Model):
    company_name = models.CharField(max_length=50)
    name_project = models.CharField(max_length=50)
    email_company = models.EmailField(max_length=20)
    logo_company = models.ImageField(upload_to='image/logo/')
    web_company =  models.URLField(default='')
    image_banner =  models.ImageField(upload_to='image/banner/')
    background_top_header = ColorField(default='#000000')
    color_top_header = ColorField(default='#ffffff')
    background_header_menu = ColorField(default='#FCCD0E')
    color_header_menu = ColorField(default='#000000')
    background_content_block = ColorField(default='#FCCD0E')
    color_content_block = ColorField(default='#000000')
    background_footer = ColorField(default='#000000')
    color_footer = ColorField(default='#ffffff')

