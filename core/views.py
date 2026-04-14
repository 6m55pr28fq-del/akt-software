from django.shortcuts import render

def home_ru(request):
    return render(request, 'core/home_ru.html')

def home_en(request):
    return render(request, 'core/home_en.html')
