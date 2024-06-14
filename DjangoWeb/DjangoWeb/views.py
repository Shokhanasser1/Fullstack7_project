from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Здесь вы можете добавить логику для обработки формы, например, отправка email или сохранение данных в базу
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
    return render(request, 'contact.html')

def products(request):
    
    products = [
        {'name': 'Продукт 1', 'description': 'Описание продукта 1.'},
        {'name': 'Продукт 2', 'description': 'Описание продукта 2.'},
        {'name': 'Продукт 3', 'description': 'Описание продукта 3.'},
    ]
    return render(request, 'products.html', {'products': products})

