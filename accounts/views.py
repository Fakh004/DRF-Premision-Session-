from rest_framework import jenerics
from .serializers import *
from .models import *

class RegisterAPIView(jenerics.CreateAPIView):
    serializer_class = RegisterSerializer
    queryset = User.objects.all()