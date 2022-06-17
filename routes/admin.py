from django.contrib import admin
from .models import MyWork,  Profile, Experience, Skills, SocialIcon 
# Register your models here.


class MyWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ['title', 'description']


admin.site.register(MyWork, MyWorkAdmin)
admin.site.register(Skills)
admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(SocialIcon)
