"""
Project related API views
"""
from django.http import JsonResponse
from rest_framework.decorators import api_view


@api_view(['GET'])
def ping(request):
    """
        monitoring api

        #### url
            /monitor/ping

        #### Method
            GET

        #### Return
            {
            "status": true,
            "statusCode": "Success",
            "statusMessage": "Success",
            "response": {
                "result": "pong"
            }
        }
    """
    response_dict = dict()
    response_dict['status'] = True
    response_dict['statusCode'] = 'Success'
    response_dict['statusMessage'] = 'Success'
    response_dict['response'] = {'result': 'pong'}
    return JsonResponse(response_dict, status=200)
