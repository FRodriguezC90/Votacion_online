from django.shortcuts import render, redirect
from .models import Candidato, Elecciones

# Instancia global de elecciones
eleccion = Elecciones()


# Create your views here.
def home(request):
    return render(request, "elecciones/home.html")


def formulario(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")

        candidato = Candidato(nombre, apellido)
        mensaje = eleccion.inscribir(candidato)  # Usamos la instancia eleccion

        return render(request, "elecciones/inscripcion.html", {"mensaje": mensaje})
    return render(request, "elecciones/formulario.html")


def inscripcion(request):
    return render(request, "elecciones/inscripcion.html")


def votar(request):
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")

        mensaje = eleccion.votar_por(
            nombre, apellido
        )  # Nota que estamos usando la instancia global 'eleccion' aquí

        return redirect(
            "registro_con_mensaje", mensaje=mensaje
        )  # Aquí es donde haces la redirección con el mensaje

    candidatos = (
        eleccion.obtener_candidatos()
    )  # Nuevamente, usa la instancia global 'eleccion'
    return render(request, "elecciones/votar.html", {"candidatos": candidatos})


def registro(request, mensaje=None):
    return render(request, "elecciones/registro.html", {"mensaje": mensaje})


def resultados(request):
    ganador = eleccion.obtener_ganador()
    empate = eleccion.hay_empate()

    if empate:
        mensaje = "No es posible determinar un ganador porque existe un empate"
    elif ganador:
        mensaje = f"El ganador es {ganador.nombre} {ganador.apellido} con {ganador.votos} votos."
    else:
        mensaje = "No hay votos registrados."

    return render(request, "elecciones/resultados.html", {"mensaje": mensaje})
