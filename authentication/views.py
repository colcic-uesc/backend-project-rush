from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.db import IntegrityError

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from .serializers import SignUpSerializer, LoginSerializer
from .models import User


class SignUpView(APIView):
    serializer_class = SignUpSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            data = request.data
            user = User.objects.create_user(
                username=data['username'],
                password=data['password'],
                email=data['email'],
                first_name=data['first_name'],
                last_name=data['last_name']
            )
            user.save()
        except IntegrityError:
            return Response("Username already exists",
                            status=status.HTTP_409_CONFLICT)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
        return Response("User created successfully",
                        status=status.HTTP_201_CREATED)


class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        try:
            data = request.data
            user = authenticate(username=data['username'],
                                password=data['password'])

            if not user:
                return Response("Invalid credentials",
                                status=status.HTTP_401_UNAUTHORIZED)

            refresh = RefreshToken.for_user(user)
            return Response(
                {
                    'message': 'User authenticated successfully',
                    'username': user.username,
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
