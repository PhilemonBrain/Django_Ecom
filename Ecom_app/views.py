from django.shortcuts import render
from django.shortcuts import render

# Create your views here.


def homeView(request):
    return render(request, "Ecom_app/index.html")