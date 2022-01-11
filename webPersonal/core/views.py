from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about/">Acerca de</a></li>
    <li><a href="/portfolio/">Portafolio</a></li>
    <li><a href="/contact/">Contacto</a></li>
</ul>
"""

def home(request):
    html_response = """
        <h2>Portada</h2>
        <p>Parrafo de home</p>
        """
    return HttpResponse(html_base+html_response)

def about(request):
    html_response = """
        <h2>Acerca de</h2>
        <p>Parrafo de acerca de</p>
        """
    return HttpResponse(html_base+html_response)

def portfolio(request):
    html_response = """
        <h2>Portafolio</h2>
        <p>Parrafo de portafolio</p>
        """
    return HttpResponse(html_base+html_response)

def contact(request):
    html_response = """
        <h2>Contacto</h2>
        <p>Parrafo de contacto</p>
        """
    return HttpResponse(html_base+html_response)