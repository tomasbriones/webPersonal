from django.shortcuts import render, HttpResponse

def home(request):
    html_response = "<h1>Mi web personal</h1><h2>portada</h2>"
    return HttpResponse(html_response)
