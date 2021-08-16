from django.shortcuts import render, HttpResponse ,redirect 
from datetime import datetime
from home.models import Contact, Signup
from django.contrib import messages


import os
from mywork.settings import BASE_DIR
from django.contrib import admin
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import path
from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from mywork.fire import isValidToken





from home.models import Books
from mywork.settings import BASE_DIR
from django.core.files.storage import FileSystemStorage
import os
import string
import random
from itertools import groupby

# Create your views here.


def index(request):
    context = {
        'variable':"this is sent"
    }
   
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
     return render(request, 'about.html',)

   # return HttpResponse("this is about page")  

def services(request):
     return render(request, 'services.html', )

    #return HttpResponse("this is services page")  



def signup(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        signup = Signup(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        signup.save()
        messages.success(request, 'Your message has been sent!')
    
    return render(request, 'signup.html')

    

    #return HttpResponse("this is services page")      

       
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    
    return render(request, 'contact.html')

    #return HttpResponse("this is contact page") 



def home(request):  
     abc=getBooks()   
     return render(request,'index.html',{'tabs':abc})

def upload(request):   
     if(request.method=='POST'):
          name = request.POST.get('name')
          author = request.POST.get('author')
          about = request.POST.get('about')
          category = request.POST.get('category')
          isForMembers = request.POST.get('isForMembers')
          fileUrl = file_uploader(request.FILES['pdf'])
          posterUrl = file_uploader(request.FILES['poster'])
          data=Books(name=name,author=author,about=about,category=category,fileUrl=fileUrl,posterUrl=posterUrl,isForMembers=True if isForMembers=='on' else False)
          data.save()          
     return render(request,'upload.html')



def file_uploader(file):
    filename=getRandomStr()+file.name  
    path=os.path.join(BASE_DIR, "static_files/"+filename)
    fs = FileSystemStorage()
    fs.save(path, file)
    return '/assets/'+filename

def getRandomStr(): 
    N = 7
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N))
    return str(res)



def getBooks():
    try:
        books= Books.objects.all().order_by('category')
    except:
        books=[]
    if(len(books)==0):
        return []
    result=[]
    temp=[]
    current=books[0].category 
    for book in books:
        if(book.category==current):
            temp.append(book)
        else:
            result.append({"tabName":temp[0].category.title() ,"books":chunkIt(temp,5)})
            current=book.category 
            temp=[]
            temp.append(book)
    
    if(len(temp)>0):
        result.append({"tabName":temp[0].category.title() ,"books":chunkIt(temp,5)})
    print(result)
    return result


def chunkIt(my_list, n):
    return [my_list[i * n:(i + 1) * n] for i in range((len(my_list) + n - 1) // n )] 



def login(request):
    return render(request,"login.html")

def create(request):
    return render(request,"create.html")

def verify(request):
    return render(request,"verify.html")

def log(request):
    if(isLoggedIn(request)==False):
        return HttpResponseRedirect("/login")

    return HttpResponse("hi there,you are now logged in")


def create_session(request):
    user=isValidToken(request)
    if(user):
        request.session["user"]=user
        return JsonResponse({"success":True})
    else:
        return JsonResponse({"success":False})


def isLoggedIn(request):
    try:
        request.session['user']
        return True
    except:
        return False