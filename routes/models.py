from os import truncate
from django.db import models

# Create your models here.
FILTER_CHOICES = (
    ('Core', 'Core'),
    ('Technology', 'Technology'),
)


class MyWork(models.Model):
    filter = models.CharField(
        max_length=30, choices=FILTER_CHOICES, default='Core')
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)
    image_url = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.description)


class Skills(models.Model):
    title = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.title, self.description)


class Profile(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    about_me = models.CharField(max_length=100, null=True, blank=True)
    desc = models.TextField(max_length=100, null=True, blank=True)
    image = models.CharField(max_length=100, null=True, blank=True)
    i_am_good_at_text = models.CharField(max_length=100, null=True, blank=True)
    my_work_text = models.CharField(max_length=100, null=True, blank=True)
    contact_text= models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.about_me)


class Experience(models.Model):
    title1 = models.CharField(max_length=30, null=True, blank=True)
    desc1 = models.TextField(max_length=300, null=True, blank=True)
    image1 = models.CharField(max_length=100, null=True, blank=True)
    title2 = models.CharField(max_length=30, null=True, blank=True)
    desc2 = models.TextField(max_length=300, null=True, blank=True)
    image2 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.title1, self.desc1)


class SocialIcon(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    url = models.CharField(max_length=50, null=True, blank=True)
    icon = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return "{}-{}-{}".format(self.name, self.icon, self.url)
