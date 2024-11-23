from django.http import HttpResponse
import datetime

def saludo(request):
  texto = "<html><body><h1>Hello World </h1></body></html"
  return HttpResponse(texto)

def fecha(request):
  miFecha = datetime.datetime.now()
  texto2 = "<html><body><h2>Fecha y hora actual: </h2>%s</body></html>" % miFecha
  return HttpResponse(texto2)

def home(request):
    return HttpResponse("<h1>Bienvenido a mi Proyecto</h1>")

# Vista para calcular la edad en determinado año
def calcEdad(request, year, edadActual):
  #edadActual = 52
  periodo = year - datetime.datetime.now().year
  edadFutura = edadActual + periodo
  documento = "<html><body><h2>En el año %s tendras %s años.</h2></body></html>" %(year, edadFutura)
  return HttpResponse(documento)
  
  