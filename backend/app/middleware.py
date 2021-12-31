try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

from django.conf import settings

class ForceDefaultLanguageMiddleware(MiddlewareMixin):
    def process_request(self, request):
        lang_code = settings.LANGUAGE_CODE

        
        if request.path.startswith("/admin/"): 
            lang_code = getattr(
                settings, 
                "ADMIN_LANGUAGE_CODE", 
                settings.LANGUAGE_CODE
            )  

        request.META['HTTP_ACCEPT_LANGUAGE'] = lang_code