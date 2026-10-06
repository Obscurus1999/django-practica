from django.shortcuts import render

# Create your views here.
def vista_dos(request):
    return render(request, 'app_dos/vista_dos.html')