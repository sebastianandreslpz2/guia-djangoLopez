from django.shortcuts import render, redirect
from django.http import HttpResponse
from inicio.models import Notebook  
from inicio.forms import BuscarNotebook, CrearNotebook
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, "inicio.html")

def otra(request):
    return render(request, "otra.html")

@login_required
def crear_notebook(request):
  
    notebook = None

    if request.method == "POST":
        formulario = CrearNotebook(request.POST, request.FILES)

        if formulario.is_valid():
            info = formulario.cleaned_data

            notebook = Notebook(modelo=info.get("modelo"), procesador=info.get("procesador"), ram=info.get("ram"), imagen=info.get("imagen"))
            notebook.save()

            return redirect("listado")
    
    else:
        formulario = CrearNotebook()

    return render(request, "crear_notebook.html",{"objeto_guardado": notebook, "formulario": formulario})

def listar_notebooks(request):

    formulario = BuscarNotebook(request.GET)
    if formulario.is_valid():
        info = formulario.cleaned_data.get("modelo")
        listado_de_notebooks = Notebook.objects.filter(modelo__icontains=info)

    return render(request, "listar_notebooks.html",{"listado_notebooks": listado_de_notebooks, "formulario": formulario})

def ver_notebook(request, notebook_id):
   
    notebook = Notebook.objects.get(id=notebook_id)
   
    return render(request, "ver_notebook.html", {"notebook": notebook})
   

class ActualizarNotebook(LoginRequiredMixin, UpdateView):

    model = Notebook
    template_name = "Actualizar_notebook.html"
    fields = '__all__'
    success_url = reverse_lazy("listado")

class EliminarNotebook(LoginRequiredMixin, DeleteView):

    model = Notebook
    template_name = "Eliminar_notebook.html"
    success_url = reverse_lazy("listado")

def about(request):
    return render(request, "about.html")
