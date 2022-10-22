
from django.shortcuts import render
from .models import place
from .models import place2
# Create your views here.


def demo(request):
  obj=place.objects.all()
  OBJ=place2.objects.all()
  return  render(request,'index.html',{'result':obj,'result2':OBJ})



