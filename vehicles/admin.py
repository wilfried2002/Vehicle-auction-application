from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('marque', 'modele', 'vendeur', 'date_ajout', 'est_vendu_badge', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="60" style="object-fit:cover;" />', obj.image.url)
        return "Aucune image"
    image_preview.short_description = "Image"

    def est_vendu_badge(self, obj):
        if obj.est_vendu:
            return format_html('<span style="color: white; background-color: green; padding: 3px 6px; border-radius: 4px;">Vendu</span>')
        return format_html('<span style="color: white; background-color: red; padding: 3px 6px; border-radius: 4px;">Disponible</span>')
    est_vendu_badge.short_description = "Statut"