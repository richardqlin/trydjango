from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request,*args,**kwargs):
	print(args,kwargs)
	print(request.user)
	return render(request,'home.html',{})

def contact_view(request,*args,**kwargs):
	
	return render(request,'contact.html',{})

def about_view(request,*args,**kwargs):
	my_context = {
		'title':'abc is about us',
		'this_is_true':True,
		'my_number':123,
		'my_list':[123,345,879,'Abc'],
		'my_html':'<h1> Hello Wolrd</h1>'
	}
	return render(request,'about.html',my_context)

def social_view(request,*args,**kwargs):
	return render(request,'social.html',{})