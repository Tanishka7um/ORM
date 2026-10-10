
from django.db import models
from django.contrib import admin
class Blinkit(models.Model):
    Number = models.IntegerField(primary_key=True)
    Otp = models.IntegerField()
    Name = models.CharField(max_length = 10)
    Email = models.EmailField()
    Address = models.TextField()
    Dob = models.DateField()
    Alternate_Number = models.IntegerField()
class BlinkitAdmin(admin.ModelAdmin):
    list_display = ["Number","Otp","Name","Email","Address","Dob","Alternate_Number"]
        
