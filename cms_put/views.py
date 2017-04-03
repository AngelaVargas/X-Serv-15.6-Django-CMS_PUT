from django.shortcuts import render
from django.http import HttpResponse
from .models import Pages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request, peticion):

	if request.method == "POST":
		p = Pages(name=request.POST['nombre'])
		p.save()

	try:
		Request = Pages.objects.get(name=peticion)
		Response = "I'm the page " + Request.name
		return HttpResponse(Response)

	except Pages.DoesNotExist:
		Response = "No existe esa página. Creala"
		Response += '<form action="" method="POST">'
		Response += 'Nombre: <input type="text" name="nombre">'
		Response += '<input type="submit" value="Enviar">'
		return HttpResponse(Response)
