from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail
from django.conf import settings


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class InstaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstaData
        fields = "__all__"