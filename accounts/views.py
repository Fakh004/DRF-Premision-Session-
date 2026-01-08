from rest_framework import generics, response, status 
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login, logout 

class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()

@api_view(['POST'])
def login_view(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        if not username or not password:
            return response({"error_message": "Fields are required"}, status=status.HTTP_400_BAD_REQUEST)
        user = authenticate
            