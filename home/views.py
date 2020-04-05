from django.shortcuts import render,HttpResponse
from home.models import Contact
# Create your views here.
def index(request):
    if request.method   =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        contact=Contact(username=username,password=password)
        contact.save()
    return render( request , 'index.html' )
def about(request):
    return HttpResponse("this is about")
def service(request):
    return HttpResponse("this is service")
