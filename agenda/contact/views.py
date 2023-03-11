from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
# Create your views here.
def index(request):
    
    contact = Contact.objects.filter(name__contains=request.GET.get("search",""))
    

    return render(request,"contact/index.html",{"contact":contact})