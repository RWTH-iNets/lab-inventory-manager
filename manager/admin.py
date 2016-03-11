from django.contrib import admin

from .models import Item, SpectrumAnalyzer, Category,\
    Inventory, SignalGenerator, ArbitaryWaveformGenerator,\
    VectorSignalGenerator, SoftwareDefinedRadio, NetworkAnalyzer,\
    Reservation
# Register your models here.

admin.site.register(Item)
admin.site.register(SpectrumAnalyzer)
admin.site.register(Category)
admin.site.register(Inventory)
admin.site.register(SignalGenerator)
admin.site.register(VectorSignalGenerator)
admin.site.register(ArbitaryWaveformGenerator)
admin.site.register(SoftwareDefinedRadio)
admin.site.register(NetworkAnalyzer)
admin.site.register(Reservation)

