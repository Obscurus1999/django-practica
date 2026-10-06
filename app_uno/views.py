from django.shortcuts import render

# Create your views here.
def inicio(request):
    lista_productos = [
        {'id': 1, 'nombre': 'Laptop Dell', 'precio': 850000},
        {'id': 2, 'nombre': 'Teclado Mecánico', 'precio': 45000},
        {'id': 3, 'nombre': 'Monitor 24"', 'precio': 120000},
    ]
    contexto = {
        'items': lista_productos
    }
    return render(request, 'app_uno/inicio.html', contexto)