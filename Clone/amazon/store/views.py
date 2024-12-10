from django.shortcuts import render
from .models import *
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .responser_serializer import*
from rest_framework import status


class RegisterUserAPI(APIView):
    def post(self, request):
        data=request.data
        fields=['name','phone_number','address','email']
        for field in fields:
            if field not in data:
                  return Response('error','please provide all required fields')  
        if Userlogin.objects.filter(phone_number=data['phone_number']).exists():
            return Response('error','phone_number is already exists',status=status.HTTP_400_BAD_REQUEST) 
        if Userlogin.objects.filter(email=data['email']).exists():
            return Response('error','email is already exists',status=status.HTTP_400_BAD_REQUEST)
        New_User=Userlogin.objects.create(
                                name=data['name'],
                                phone_number=data['phone_number'],
                                address=data['address'],
                                email=data['email'])
        New_User.save()
        return Response('Register User Successfully',status=status.is_success)


class ProductView(View):
    def get(self,request):
        products = Product.objects.all()
        return render(request, 'product_details.html', {'products': products})
    
class ProductDetail(APIView):
    def get(self, request):
        data=request.data
        product = get_object_or_404(Product, id=data['id'])
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    

    

      