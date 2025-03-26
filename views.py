from django.shortcuts import render,redirect
from django.contrib import messages
from portpolio.models import Contact,Blogs,Internship,Certificate
# Create your views here.
def home(request):
    return render(request,'home.html')

def handleblog(request):
    posts=Blogs.objects.all()
    context={"posts":posts}
    return render(request,'handleblog.html',context)

def certificate_View(request):
    docs=Certificate.objects.all()
    context={"docs":docs}
    return render(request,'certificate.html',context)


def about(request):
    return render(request,'about.html')


def internshipdetails(request):

    if not request.user.is_authenticated:
        messages.warning(request,"Please login to access this page")
        return redirect("/auth/login/")

    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fusn=request.POST.get('usn')
        fphone=request.POST.get('phonenumber')
        fcollege=request.POST.get('cname')
        foffer=request.POST.get('offer')
        fstartdate=request.POST.get('startdate')
        fenddate=request.POST.get('enddate')
        fprojreport=request.POST.get('projreport')
        file_upload=request.POST.get('my_file')

# converting to upper case
        fname=fname.upper()
        fusn=fusn.upper()
        fcollege=fcollege.upper()
        fprojreport=fprojreport.upper()
        foffer=foffer.upper()

        # 
        check1=Internship.objects.filter(phonenumber=fphone).exists()
        check2=Internship.objects.filter(email=femail).exists()

        if check1 or check2:
            messages.warning(request,"Your Details are Stored Already")
            return redirect("/internshipdetails")
        



        query=Internship(fullname=fname,usn=fusn,phonenumber=fphone,email=femail,college_name=fcollege,offer_status=foffer,start_date=fstartdate,end_date=fenddate,proj_report=fprojreport,my_file=file_upload)
        query.save()

        messages.success(request,"Form is Submitted Successful!")
        return redirect('/internshipdetails')

    return render(request,'intern.html')
# ................................................................................
def show_file(request):
    all_data=Internship.objects.all()
    context={
        'datta':all_data
    }
    return render(request,'view.html',context)

# .....................................................................................

def contact(request):
    if request.method=="POST":
        fname=request.POST.get('name')
        femail=request.POST.get('email')
        fphoneno=request.POST.get('num')
        fdesc=request.POST.get('desc')
        query=Contact(name=fname,email=femail,phonenumber=fphoneno,description=fdesc)
        query.save()
        messages.success(request,"Thanks for contacting us. We will get by you Soon!")

        return redirect('/contact')

    return render(request,'contact.html')

from django.http import HttpResponse


# def chatbot(request):
#     return render(request,'chatbot.html')