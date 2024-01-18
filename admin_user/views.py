from django.shortcuts import render, HttpResponse, redirect
from app.models import Producto
from decimal import Decimal
from app.form import FormularioArticulo

# Create your views here.


def admin_add_product(request):
    productos = Producto.objects.all()
    return render(request, 'admin/add_product.html', {
        'productos': list(productos),
        'cantidad': len(productos)
    })


def save_product(request):
    if request.method == 'POST':
        producto = Producto(
            nombre=request.POST['nombre'],
            precio=Decimal(request.POST['precio']),
            fabricante=request.POST['fabricante']
        )
        producto.save()
        return redirect('index')
    else:
        return redirect('add_product')


def create_form_article(request):
    formulario = FormularioArticulo()
    return render(request, 'form_article.html', {
        'formulario': formulario
    })
