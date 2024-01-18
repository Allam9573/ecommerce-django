from django.shortcuts import render

# Create your views here.


def admin_add_product(request):
    return render(request, 'admin/add_product.html')
