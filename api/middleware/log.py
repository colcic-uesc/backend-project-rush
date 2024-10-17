from django.utils import timezone
from api.models import Log


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start = timezone.now()

        response = self.get_response(request)

        total_time = timezone.now() - start

        log = {
            "client_ip": request.META.get("REMOTE_ADDR"),
            "has_jwt": request.user.is_authenticated,
            "request_date": timezone.now(),
            "request_method": request.method,
            "request_total_time": total_time,
        }

        Log.objects.create(**log)

        return response
