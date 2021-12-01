from django.shortcuts import render
from .serializers import RegisterSerializer

from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

# Create your views here.
class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message":"User successfully created."
        })