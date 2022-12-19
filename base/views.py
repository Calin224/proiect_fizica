from django.shortcuts import render

# Create your views here.

def homePage(request):
    return render(request, 'base/home.html')

def circuitPage(request):
    return render(request, 'base/circuit.html')

def miscariPage(request):
    return render(request, 'base/miscariOscilatorii.html')