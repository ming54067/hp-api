from django.contrib import admin
from .models import Property
from .models import Customer
from .models import Owner
from .models import Reservation


# Register your models here.
admin.site.register(Property)
admin.site.register(Customer)
admin.site.register(Owner)
admin.site.register(Reservation)