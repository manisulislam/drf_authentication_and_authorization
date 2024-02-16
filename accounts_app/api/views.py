from .serializers import RegisterSerializers
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

@api_view(['POST'])
def RegisterView(request):
    serializer = RegisterSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logoutView(request):
    return request.user.auth_token.delete()