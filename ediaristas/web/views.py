from django.shortcuts import redirect, render
from .forms import diarista_form, contratante_form
from .models import Diarista, Contratante

# Create your views here.

# Diaristas
def cadastrar_diarista(request):
    if request.method == 'POST':
        form_diarista = diarista_form.DiaristaForm(request.POST, request.FILES)
        if form_diarista.is_valid():
            form_diarista.save()
            return redirect('listar_diaristas')
    else:
        form_diarista = diarista_form.DiaristaForm()
    return render(request, 'form_diarista.html', {'form_diarista': form_diarista})

def listar_diaristas(request):
    diaristas = Diarista.objects.all()
    return render(request, 'lista_diaristas.html', {'diaristas': diaristas})

def editar_diarista(request, diarista_id):
    diarista = Diarista.objects.get(id=diarista_id)
    if request.method == 'POST':
        form_diarista = diarista_form.DiaristaForm(request.POST or None, request.FILES, instance=diarista)
        if form_diarista.is_valid():
            form_diarista.save()
            return redirect('listar_diaristas')
    else:
        form_diarista = diarista_form.DiaristaForm(instance=diarista)
    return render(request, 'form_diarista.html', {'form_diarista': form_diarista})

def remover_diarista(request, diarista_id):
    diarista = Diarista.objects.get(id=diarista_id)
    diarista.delete()
    return redirect('listar_diaristas')

# Contratantes
def cadastrar_contratante(request):
    if request.method == 'POST':
        form_contratante = contratante_form.ContratanteForm(request.POST, request.FILES)
        if form_contratante.is_valid():
            form_contratante.save()
            return redirect('listar_contratantes')
    else:
        form_contratante = contratante_form.ContratanteForm()
    return render(request, 'form_contratante.html', {'form_contratante': form_contratante})

def listar_contratantes(request):
    contratantes = Contratante.objects.all()
    return render(request, 'lista_contratantes.html', {'contratantes': contratantes})