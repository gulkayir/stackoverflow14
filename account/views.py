from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import MyUser
from account.serializers import RegisterSerializer


class RegisterView(APIView):

    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Successfully registered on StackOverflow!', status=status.HTTP_201_CREATED)

class ActivateView(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('activation_code')
        user = MyUser.objects.filter(phone_number=phone_number, activation_code=code).first()
        if not user:
            return Response('User not found', status=status.HTTP_400_BAD_REQUEST)
        user.is_active=True
        user.activation_code = ''
        user.save()
        return Response('You successfully activated your account', status=status.HTTP_200_OK)


