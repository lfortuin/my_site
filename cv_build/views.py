from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io

# Create your views here.
def info(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        phone=request.POST.get("phone","")
        email=request.POST.get("email","")
        secondary_education=request.POST.get("secondary_education","")
        tertiary_education=request.POST.get("tertiary_education","")
        degree_name=request.POST.get("degree_name","")
        skill_set=request.POST.get("skill_set","")
        personal_statement=request.POST.get("personal_statement","")
        previous_work=request.POST.get("previous_work","")

        profile=Profile(name=name,phone=phone,email=email,secondary_education=secondary_education,tertiary_education=tertiary_education,degree_name=degree_name,skill_set=skill_set,personal_statement=personal_statement,previous_work=previous_work)
        profile.save()
    return render(request, "list_of_users.html")

def build_cv(request,id):
    profile_of_user=Profile.objects.get(pk=id)
    template = loader.get_template("build_cv.html")
    html = template.render({'profile_of_user':profile_of_user})
    option={
        'page-size':'Letter',
        'endcoding':'UTF-8'
        }
    pdf = pdfkit.from_string(html, False, option)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Contents-Disposition']="attachments"
    return response

def list_of_users(request):
    profile = Profile.objects.all()
    return render(request, "list_of_users.html",{'profile':profile})