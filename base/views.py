
from django.shortcuts import render
from .serializers import Exmapleserializer
from .models import Exmpale
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.parsers import MultiPartParser, FormParser

# register api_view #
@api_view(['POST'])
def register(request):
    user = User.objects.create_user(username= request.data["username"],password=request.data['password'],is_staff=1,is_superuser=1)
    return Response({"reg":"test"})



class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            response.data['message'] = 'Login successful.'
        else:
            response.data['message'] = 'Invalid login credentials.'
        return response

# <------------------------------------------------Your model Entry Points --------------------------------------->
class Your_Model_ViewSet(APIView):
    def get(self, request):
        my_model = Exmpale.objects.all()
        serializer = Exmapleserializer(my_model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Exmapleserializer(data=request.data, context={'user': request.user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
    def put(self, request, pk):
        my_model = Exmpale.objects.get(pk=pk)
        serializer = Exmapleserializer(my_model, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

    def delete(self, request, pk):
        my_model = Exmpale.objects.get(pk=pk)
        my_model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

 # <--------------------------------------------------- images entry Points ------------------------------------------->
@api_view(['GET'])
def getImages(request):
    res=[] #create an empty list
    for img in Exmpale.objects.all(): #run on every row in the table...
        res.append({
                 "image":str( img.image)
                }) #append row by to row to res list
    return Response(res) #return array as json response


# upload image method (with serialize)
class APIViews(APIView):
    parser_class=(MultiPartParser,FormParser)
    def post(self,request,*args,**kwargs):
        api_serializer=Exmapleserializer(data=request.data)
       
        if api_serializer.is_valid():
            api_serializer.save()
            return Response(api_serializer.data,status=status.HTTP_201_CREATED)
        else:
            print('error',api_serializer.errors)
            return Response(api_serializer.errors,status=status.HTTP_400_BAD_REQUEST)