from django.contrib import admin
from .models import Charity
# Register your models here.


class CharityAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

admin.site.register(Charity, CharityAdmin)