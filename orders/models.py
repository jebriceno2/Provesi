from django.db import models

class Pedido(models.Model):
    class Estado(models.TextChoices):
        CREADO     = "CREADO"
        PAGADO     = "PAGADO"
        DESPACHADO = "DESPACHADO"
        ENTREGADO  = "ENTREGADO"
        CANCELADO  = "CANCELADO"

    pedido_id = models.CharField(max_length=64, unique=True, db_index=True)
    estado    = models.CharField(max_length=16, choices=Estado.choices)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "pedidos"

