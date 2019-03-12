import json
import logging
from django.http import JsonResponse


def respone_json(success, message, data):
    result = {
        "success": success,
        "message": message,
        "data": data,
    }
    return JsonResponse(result, safe=False)


def respone_success(data={}):
    return respone_json(True, "", data)


def respone_failed(message):
    return respone_json(False, message, {})


logger = logging.getLogger(__name__)
