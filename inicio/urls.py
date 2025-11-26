from django.urls import path  
from .views import inicio, otra, crear_notebook, listar_notebooks, ver_notebook, ActualizarNotebook, EliminarNotebook, about

urlpatterns = [
    path("", inicio, name="inicio"),
    path("otra/", otra, name="otra"),
    path("ver-notebooks/<notebook_id>", ver_notebook, name="ver"),
    path("Actualizar-notebooks/<pk>", ActualizarNotebook.as_view(), name="Actualizar"),
    path("Eliminar-notebooks/<pk>", EliminarNotebook.as_view(), name="Eliminar"),
    path("crear-notebook/", crear_notebook, name="crear"),
    path("listado-notebooks/", listar_notebooks, name="listado"),
    path("about/", about, name="about"),

]

