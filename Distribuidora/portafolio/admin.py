from django.contrib import admin
from .models import Producto,category


# Register your models here.

class CategoryaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class projectAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'descripcion', 'precio')
    search_fields = ('nombre_producto', 'descripcion', 'precio')
    list_filter = ('nombre_producto', 'descripcion', 'precio')
    readonly_fields = ('creado','actualizado')


admin.site.register(Producto,projectAdmin)
admin.site.register(category,CategoryaAdmin)