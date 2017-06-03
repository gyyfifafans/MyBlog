from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User


# Create your views here
#form
class UserForm(forms.Form):
    username = forms.CharField(label='Username',max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput())

#regist
def regist(req):
   if req.method == 'POST':
       uf = UserForm(req.POST)
       print uf
       print req.POST
       if uf.is_valid():
           #get form data
           username = uf.cleaned_data['username']
           password = uf.cleaned_data['password']
           #add to database
           User.objects.create(username=username,password=password)
           return HttpResponse('regist success!!')
   else:
       uf = UserForm()
   return render_to_response('regist.html',{'uf':uf},context_instance=RequestContext(req))


#login
def login(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        print req.POST
	print uf
        s=req.POST['gender']
        print s
        #if uf.is_valid():
        if True:
            #get data from database
            #usrname=uf.cleaned_data['username']
            #pwd=uf.cleaned_data['password']
            usrname=req.POST['name']
            pwd=req.POST['password']
            #check input data with data where in database
            user = User.objects.filter(username = usrname,password = pwd)
            if user:
                #success go into index
                response = HttpResponseRedirect('/index/')
                #write in cookie,lost time is 3600
                response.set_cookie('username',usrname,3600)
                return response
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf},context_instance=RequestContext(req))


#login success

def index(req):
    username = req.COOKIES.get('username','')
    print username
    return render_to_response('index.html',{'username':username})

#logout
def logout(req):
    response =HttpResponse('logout !!')
    #clean cookies
    response.delete_cookie('username')
    return response


#test
def test(req):
    return render_to_response('test.html')


#replace
def replace(request): 
    return render_to_response('CheckAttendanceInfoView.html')
