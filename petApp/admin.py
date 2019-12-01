from django.contrib import admin
from petApp.models import Pet

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    pass
