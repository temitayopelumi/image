from django.shortcuts import render
from .models import Image
from .serializer import ImageSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


# from rest_flex_fields.views import FlexFieldsModelViewSet

@api_view(['POST', ])
def addImage(request):
    serializers = ImageSerializer(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)