from django.contrib import admin
from .models import House
from .models import Address
from .models import Image
from .models import Amenity
from .models import Bedroom
from .models import Bed


# Register your models here.
admin.site.register(House)
admin.site.register(Address)
admin.site.register(Image)
admin.site.register(Amenity)
admin.site.register(Bed)
admin.site.register(Bedroom)

