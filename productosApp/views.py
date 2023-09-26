from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'productosApp/index.html')

def electronica(request):
    data = {
        'titulo': 'Electronica',
        'marca1': 'Sony',
        'producto1': 'LED 50"',
        'descrip1': 'Sirve para ver anime en 4K',
        'img1': 'https://falabella.scene7.com/is/image/Falabella/14591573_1?wid=800&hei=800&qlt=70',
        'marca2': 'Samsung',
        'producto2': 'LED 40"',
        'descrip2': 'Sirve para ver anime en 4K',
        'marca3': 'LG',
        'producto3': 'LED 30"',
        'descrip3': 'Sirve para ver anime en 4K',
    }
    return render(request, 'productosApp/productos.html', data)

def ropa(request):
    data = {
        'titulo': 'Ropa'
    }
    return render(request, 'productosApp/productos.html', data)

def consolas(request):
    data = {
        'titulo': 'Consolas'
    }
    return render(request, 'productosApp/productos.html', data)