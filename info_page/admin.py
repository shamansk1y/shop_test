from django.contrib import admin
from .models import InfoPage



@admin.register(InfoPage)
class InfoPageAdmin(admin.ModelAdmin):
    model = InfoPage
    list_display = ['title']
