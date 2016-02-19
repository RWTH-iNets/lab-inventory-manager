from django.contrib import admin

from .models import Item, SpectrumAnalyzer, Category, Inventory, SignalGenerator
# Register your models here.

admin.site.register(Item)
admin.site.register(SpectrumAnalyzer)
admin.site.register(Category)
admin.site.register(Inventory)
admin.site.register(SignalGenerator)

