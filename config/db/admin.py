from django.contrib import admin

# Register your models here.

from .models import Delivery,ClinicManager,Item,Order

admin.site.register(Delivery)
admin.site.register(Item)
admin.site.register(Order)
admin.site.register(ClinicManager)
