from django.contrib import admin

from .models import Item, ItemDescriptor, SpectrumAnalyzer, Category,\
    SignalGenerator, NetworkAnalyzer, Reservation
# Register your models here.

admin.site.register(Item)
admin.site.register(ItemDescriptor)
admin.site.register(SpectrumAnalyzer)
admin.site.register(Category)
admin.site.register(SignalGenerator)
admin.site.register(NetworkAnalyzer)
admin.site.register(Reservation)

