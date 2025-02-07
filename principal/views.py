from django.shortcuts import render, redirect
from .models import MyTable
from .forms import CedulaForm

def buscar_ci(request):
    form = CedulaForm()
    resultados = []

    # Comprobamos si se envía un POST
    if request.method == "POST":
        if "clear" in request.POST:
            # Redirige a GET limpio para borrar datos de búsqueda
            return redirect("index")  # Redirige para limpiar los datos del formulario

        form = CedulaForm(request.POST)
        if form.is_valid():
            ci_titular = form.cleaned_data["ci_titular"]
            if ci_titular:
                resultados = MyTable.objects.filter(ci_titular=ci_titular)

    return render(request, "index.html", {"form": form, "resultados": resultados})
