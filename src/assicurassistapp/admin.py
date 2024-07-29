from django.contrib import admin
from .models import (Cliente, Veicolo, Compagnia,
                    Polizza, Broker)

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Veicolo)
admin.site.register(Compagnia)
admin.site.register(Polizza)
admin.site.register(Broker)

