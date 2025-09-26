from django.contrib import admin
from .models import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display  = ("pedido_id", "estado", "updated_at")
    search_fields = ("pedido_id",)
    list_filter   = ("estado",)

