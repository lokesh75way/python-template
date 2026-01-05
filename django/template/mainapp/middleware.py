import time
import logging

logger = logging.getLogger(__name__)

# 4.5 Middleware & Signals (Middleware lifecycle)
class TimingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        
        response = self.get_response(request)
        
        duration = time.time() - start_time
        logger.info(f"Request to {request.path} took {duration:.2f} seconds")
        
        # Add header to response
        response['X-Request-Duration'] = str(duration)
        
        return response
