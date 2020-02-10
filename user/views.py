from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import requests
from .serializers import CreateUserSerializer
from django.conf import settings

CLIENT_ID = 'pBCOrq5d1EMQwLOdpS9Jx6n7qweHyxazTBAOsrR7'
CLIENT_SECRET = 'BZbMf364bDEP5Q9WYSgG6EA5FlnpBMh2gOGYmwvghQ3p4NETgLwoTOWgmCm5iBA7SCQi7nATFhoCdZAdJGUxQfehL1M704Ucyw6E0ebYm0JDuJPomZMnPBUlShFaR157'

@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    print(request.build_absolute_uri() )
    serializer = CreateUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        r = requests.post('http://localhost:8000/o/token/',
            data={
                'grant_type' : 'password',
                'username' : request.data['username'],
                'password' : request.data['password'],
                'client_id' : request.data['client_id'],
                'client_secret' : request.data['client_secret'],
            }
        )
        return Response(r.json())
    return Response(serializer.errors)

@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    print(request.data)
    r = requests.post('http://localhost:8000/o/token/',
        data={
            'grant_type' : 'password',
            'username' : request.data['username'],
            'password' : request.data['password'],
            'client_id' : request.data['client_id'],
            'client_secret' : request.data['client_secret'],
        }
    )
    return Response(r.json())

@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    r = requests.post('http://localhost:8000/o/token',
        data={
            'grant_type' : 'refresh_token',
            'refresh_token' :  request.data['refresh_token'],
            'client_id' : request.data['client_id'],
            'client_secret' : request.data['client_secret'],
        }
    )
    return Response(r.json())

@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    r = requests.post('http://localhost:8000/o/revoke_token',
        data={
            'token' : request.data['token'],
            'client_id' : request.data['client_id'],
            'client_secret' : request.data['client_secret'],
        }
    )
    
    if r.status_code == requests.codes.ok :
        return Response({'message' : 'token revoked'}, r.status_code)
    
    return Response(r.json(), r.status_code)