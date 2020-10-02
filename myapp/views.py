from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Document, Python, C, Html, Java, Javascript, Css, Django

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        pswd = request.POST.get('pswd', '')
        c_pswd = request.POST.get('c_pswd', '')
        if pswd==c_pswd:
            student = Student(name=name, email=email, phone=phone, pswd=pswd)
            student.save()
            thank = True
            msg = 'registration sucessful.'
            return render(request,'register.html',{'thank':thank,'msg':msg})
        else:
            thank = True
            msg = 'Password does not match'
            return render(request,'register.html',{'thank':thank,'msg':msg})
    else:
        return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email', '')
        pswd = request.POST.get('pswd', '')
        if (Student.objects.filter(email=email,pswd=pswd)):
            request.session['id'] = 1
        # if(email==c_email and pswd==c_pswd):
            thank = True
            return redirect('/webtut/home')
        else:
            error = True
            msg = 'Invalid credantials'
            return render(request,'login.html',{'msg':msg,'error':error})
    return render(request,'login.html')

def download(request):
    if "id" in request.session:
        doc = Document.objects.all()
        return render(request,'download.html',{'doc':doc})
    else:
        return redirect('/webtut/home')

def logout(request):
    # del  request.session['id']
    request.session.clear()
    return redirect('/webtut/home')

def python(request):
    if "id" in request.session:
        video = Python.objects.all()
        return render(request, 'course/python.html',{'video':video})
    else:
        return redirect('/webtut/home')
        
def c(request):
    if "id" in request.session:
        video = C.objects.all()
        return render(request, 'course/C.html',{'video':video})
    else:
        return redirect('/webtut/home')

def html(request):
    if "id" in request.session:
        video = Html.objects.all()
        return render(request, 'course/html.html',{'video':video})
    else:
        return redirect('/webtut/home')

def css(request):
    if "id" in request.session:
        video = Css.objects.all()
        return render(request, 'course/css.html',{'video':video})
    else:
        return redirect('/webtut/home')

def django(request):
    if "id" in request.session:
        video = Django.objects.all()
        return render(request, 'course/django.html',{'video':video})
    else:
        return redirect('/webtut/home')

def java(request):
    if "id" in request.session:
        video = Java.objects.all()
        return render(request, 'course/java.html',{'video':video})
    else:
        return redirect('/webtut/home')
    
def javascript(request):
    if "id" in request.session:
        video = Javascript.objects.all()
        return render(request, 'course/javascript.html',{'video':video})
    else:
        return redirect('/webtut/home')
