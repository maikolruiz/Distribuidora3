from django.contrib import admin
from .models import links
from .models import categoria

# Register your models here.

class linksAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')

class categoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('creado','actualizado')


admin.site.register(links,linksAdmin)
admin.site.register(categoria,categoriaAdmin)
