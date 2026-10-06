from django.shortcuts import render

# Create your views here.
def vista_tres(request):
    return render(request, 'app_tres/vista_tres.html')