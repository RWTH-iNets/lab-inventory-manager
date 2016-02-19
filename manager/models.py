from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=1024)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=1024)
    category = models.ManyToManyField(Category)
    img_url = models.CharField(max_length=1024, blank = True, null = True)
    doc_url = models.CharField(max_length=1024, blank = True, null = True)

    def __str__(self):
        return self.name

class SpectrumAnalyzer(Item):
    freq_start = models.IntegerField(blank = True, null = True)
    freq_stop = models.IntegerField(blank = True, null = True)
    input_power_max = models.IntegerField(blank = True, null = True)

class SignalGenerator(Item):
    freq_start = models.IntegerField(blank = True, null = True)
    freq_stop = models.IntegerField(blank = True, null = True)
    output_power_max = models.IntegerField(blank = True, null = True)

class Inventory(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    count = models.IntegerField()
