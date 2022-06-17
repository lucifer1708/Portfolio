from django.shortcuts import render
from .models import MyWork, Profile, Experience, SocialIcon, Skills

# Create your views here.


# class MyWorkList(generic.ListView):
#     model = MyWork
#     template_name = 'index.html'
#     context_object_name = 'work_list'

def Index(request):
    profiles = Profile.objects.all()
    work_list = MyWork.objects.all()
    experience = Experience.objects.all()
    social = SocialIcon.objects.all()
    skills = Skills.objects.all()
    ctx = {'profiles': profiles, 'work_list': work_list,
           'experience': experience, 'social': social, 'skills': skills}
    return render(request, 'index.html', ctx)
