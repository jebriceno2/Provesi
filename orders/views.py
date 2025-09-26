from django.http import JsonResponse, HttpResponseNotFound
from django.core.cache import cache
from .models import Pedido

def estado(request, pedido_id: str):
    key = f"estado:{pedido_id}"
    data = cache.get(key)
    if data:
        return JsonResponse(data, status=200)

    try:
        p = (Pedido.objects
                     .only("pedido_id","estado","updated_at")
                     .get(pedido_id=pedido_id))
    except Pedido.DoesNotExist:
        return HttpResponseNotFound()

    data = {
        "pedidoId": p.pedido_id,
        "estado": p.estado,
        "ultimaActualizacion": p.updated_at.isoformat()
    }
    cache.set(key, data, timeout=120)  # 2 min
    return JsonResponse(data, status=200)
