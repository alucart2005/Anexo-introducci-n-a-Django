from clientes.models import Cliente, Factura
import datetime

clientes = Cliente.objects.all()
for cliente in clientes:
    print(f"Nombre: {cliente.nombre}, Apellidos: {cliente.apellidos}")
    
