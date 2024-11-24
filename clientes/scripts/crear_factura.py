import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'miProyecto.settings')
django.setup()

from clientes.models import Cliente, Factura
import datetime

# Crear la fecha de nacimiento de Pedro
fecha_nacimiento = datetime.date(1980, 12, 5)

# Crear el cliente Pedro
pedro = Cliente.objects.create(
    nombre="Pedro",
    apellidos="Aguilar Ramírez",
    rfc="AGRM-801205-111",
    fecha_nacimiento=fecha_nacimiento,
    activo=True,
)

# Crear la factura asociada a Pedro
Factura.objects.create(
    cliente=pedro,
    importe=5690.12,
    pagada=False
)
