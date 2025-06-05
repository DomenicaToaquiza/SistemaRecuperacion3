from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from .models import Monumento

def inicio(request):
    return render(request, 'listarMonumento.html') 

# LISTADO DE MONUMENTOS
def listar_monumento(request):
    monumentos = Monumento.objects.all()  # Obtiene todos los monumentos
    return render(request, "listarMonumento.html", {'monumentos': monumentos})

# FORMULARIO NUEVO MONUMENTO
def nuevo_monumento(request):
    return render(request, "nuevoMonumento.html")

def guardar_monumento(request):
    if request.method == 'POST':  # Asegúrate de que es un POST
        nombre = request.POST["nombre"]
        ubicacion = request.POST["ubicacion"]
        descripcion = request.POST["descripcion"]
        imagen = request.FILES.get("imagen")  # Obtener la imagen subida
        
        # Crear un nuevo Monumento
        Monumento.objects.create(
            nombre=nombre,
            ubicacion=ubicacion,
            descripcion=descripcion,
            imagen=imagen
        )
        
        # Mostrar mensaje de éxito
        messages.success(request, "Monumento guardado exitosamente")
        
        # Redirigir a la lista de monumentos
        return redirect('listar_monumento')
    else:
        # Si no es un POST, redirigir de vuelta a la página de nuevo monumento
        return redirect('nuevo_monumento')

# ELIMINAR MONUMENTO
def eliminar_monumento(request, id):
    monumento = get_object_or_404(Monumento, id=id)
    
    if monumento.imagen:
        monumento.imagen.delete()  # Borra el archivo de imagen si existe

    monumento.delete()
    messages.success(request, "Monumento eliminado exitosamente")
    return redirect('listar_monumento')  # Redirige a la lista de monumentos

# EDITAR MONUMENTO
def editar_monumento(request, id):
    monumento = get_object_or_404(Monumento, id=id)
    return render(request, "editarMonumento.html", {'monumentoEditar': monumento})

# PROCESAR EDICIÓN
def procesar_edicion_monumento(request):
    id = request.POST["id"]
    monumento = get_object_or_404(Monumento, id=id)

    monumento.nombre = request.POST["nombre"]
    monumento.ubicacion = request.POST["ubicacion"]
    monumento.descripcion = request.POST["descripcion"]

    # MANEJO DE LA IMAGEN (solo si se sube una nueva)
    if 'imagen' in request.FILES:
        if monumento.imagen:
            monumento.imagen.delete()  # Elimina la imagen anterior
        monumento.imagen = request.FILES['imagen']  # Asigna la nueva imagen
    
    monumento.save()
    messages.success(request, "Monumento actualizado exitosamente")
    return redirect('listar_monumento')  # Redirige a la lista de monumentos