from django.shortcuts import render,redirect
from django.http import HttpResponse
from xv.models import Invitado
from xv.forms import InvitadoForm

def invitacion(request):
    if request.method == 'POST':
        form = InvitadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('confirmacion')

    else:
        form = InvitadoForm()

    context = {'form': form}
    return render(request, 'invitacion.html', context)
    
def invitados(request):
    invitados = Invitado.objects.all()
    context = {'invitados': invitados}
    return render(request, 'invitados.html', context)

def confirmacion(request):
    return render(request, 'confirmacion.html')