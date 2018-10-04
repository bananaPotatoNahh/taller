from django.shortcuts import render, HttpResponse

from .models import Persona

# Create your views here.
def index(request):
    personas = Persona.objects.all()
    return render(request, 'persona/index.html', {'personas': personas})

def create(request):
    if request.POST:
        nombre = request.POST.get('nombre', None)
        persona = Persona()
        persona.nombre = nombre
        persona.apellidoPaterno = 'No Tengo'
        persona.save()

        return render(request, 'persona/show.html', {'minombre': persona.nombre})

    return render(request, 'persona/create.html', {})