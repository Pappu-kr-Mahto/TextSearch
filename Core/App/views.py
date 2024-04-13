from django.shortcuts import render , HttpResponse

from django.contrib.auth import authenticate
from .serializers import *
from .models import *

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken

import string
from collections import Counter

# Create your views here.

def home(request):
    return HttpResponse(" server is live ")

@api_view(['POST'])
def signup(request):
    try:
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user=CustomUserModel.objects.create_user(email = serializer.validated_data['email'] , username=serializer.validated_data['username'] , dob= serializer.validated_data['dob'] , password = serializer.validated_data['password'])

            return Response({"msg":"Account Created successfully","username":request.data['username'],"email":request.data['email']},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    except Exception as e:
        return Response({"error":'Internal server Error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['POST'])
def login(request):
    try:
        email= request.data.get('email')
        password = request.data.get('password')
        if email is None or password is None:
            return Response({'message': 'Please provide both email and password'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = CustomUserModel.objects.filter(email=email).first()
        print(user.username)
        if user is not None:
            temp = authenticate(email=user.email, password=password)
            if temp is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                        'user':email,
                        'access': str(refresh.access_token),
                        'refresh': str(refresh),
                    })
        return Response({"error":"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)
    
    except Exception as e:
        return Response({"error":"Invalid Credentials"},status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def allParagraph(request):
    try:
        user = CustomUserModel.objects.get(email = request.user)
        data = Paragraph.objects.filter(user = user).values()
        return Response(data,status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'error':'Internal Server Error '},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addParagraph(request):
    try:
        user = CustomUserModel.objects.get(email=request.user)
        print(user)
        data = request.data['paragraph']
        print(data)

        for para in data:
            paraObj = Paragraph.objects.create(paragraph=para, user=user)
            punctuation = set(string.punctuation)

            cln_para = ""
            for chr in para.lower():
                if chr not in punctuation:
                    cln_para+=chr
            
            para_list = cln_para.split(" ")
            worddict=dict(Counter(para_list))

            wordInstance=[]
            for text in worddict.keys():
                wordInstance.append(WordsTokanize(word=text, occurrence=worddict[text], paragraph=paraObj, user=user))
            WordsTokanize.objects.bulk_create(wordInstance)    
        return Response({'success': 'Paragraph added successfully'},status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({"error":'Internal server Error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def wordSearch(request,word):
    try:
        user = CustomUserModel.objects.get(email = request.user)
        data=WordsTokanize.objects.filter(word=word , user=user).values().order_by('-occurrence')[:10]
        para_ids = [ob.get('paragraph_id', 0) for ob in data]
        para_data=Paragraph.objects.filter(id__in=para_ids,user=user).values()
        return Response({'data': para_data},status=status.HTTP_200_OK)
        
    except Exception as e:
        print(e)
        return Response({"error":'Internal server Error'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)