from django.shortcuts import render

def swagger_ui_view(request):
    return render(request, 'swagger.html')

def redoc_ui_view(request):
    return render(request, 'redoc.html')