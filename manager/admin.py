from django.contrib import admin

from .models import Item, ItemDescriptor, Reservation, ErrorReport, Category, SpectrumAnalyzer,\
    SignalGenerator, NetworkAnalyzer, Oscilloscope 
# Register your models here.

admin.site.register(Item)
admin.site.register(ItemDescriptor)
admin.site.register(Reservation)
admin.site.register(ErrorReport)
admin.site.register(Category)

admin.site.register(SpectrumAnalyzer)
admin.site.register(SignalGenerator)
admin.site.register(NetworkAnalyzer)
admin.site.register(Oscilloscope)

