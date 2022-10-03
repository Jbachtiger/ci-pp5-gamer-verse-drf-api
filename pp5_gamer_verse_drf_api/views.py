from rest_framework.decorators import api_view
from rest_framework.response import Response

# DRF-API walkthrough used to get guidance

@api_view()
def root_route(request):
    return Response({
        "message": 'Welcome to the Gamer Verse API!'
    })
