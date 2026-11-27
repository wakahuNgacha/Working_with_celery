import json

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

from .tasks import shared_task

@csrf_exempt
@require_POST
def multiplayer(request):
    try:
        payload = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "Request body must be valid JSON."}, status=400)

    if not isinstance(payload, dict):
        return JsonResponse({"error": "JSON body must be an object."}, status=400)

    values = (payload.get("r"), payload.get("x"))
    if any(
        isinstance(value, bool)
        or not isinstance(value, (int, float))
        for value in values
    ):
        return JsonResponse(
            {"error": "Fields 'r' and 'x' must be numbers."}, status=400
        )

    answer = shared_task(*values)
    return JsonResponse({"answer": answer})
