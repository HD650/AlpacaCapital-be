from backend import  settings
from django.utils.deprecation import MiddlewareMixin
# to globally disable csrf


class DisableCSRF(MiddlewareMixin):

    def process_request(self, req):
        # only disbale when debug
        if settings.DEBUG:
            attr = '_dont_enforce_csrf_checks'
            if not getattr(req, attr, False):
                setattr(req, attr, True)
