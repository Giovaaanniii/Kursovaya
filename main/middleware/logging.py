from django.core.cache import cache
from django.conf import settings
import re
import time

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if self.is_excluded(self, request.path):
            return response

        user_id = request.user.id if request.user.is_authenticated else None

        log_entry = {
            'user_id': user_id,
            'method': request.method,
            'path': request.path,
            'status_code': response.status_code,
            'client_ip': request.META.get('REMOTE_ADDR'),
            'user_agent': request.META.get('HTTP_USER_AGENT', '<unknown>'),
            'timestamp': time.time()
        }

        log_data = cache.get('request_logs', [])
        log_data.append(log_entry)

        cache.set('request_logs', log_data, timeout=120)

        return response

    @staticmethod
    def is_excluded(self, path):
        excluded_paths = getattr(settings, 'EXCLUDED_URLS_FROM_LOGGING', [])
        for pattern in excluded_paths:
            if re.match(pattern, path):
                return True
        return False
