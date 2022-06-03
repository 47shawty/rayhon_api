from django.contrib.auth import authenticate
from django.db import IntegrityError
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets, generics, permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http import JsonResponse

# Create your views here.
from rest_framework.permissions import IsAuthenticated

from api.serializers import *
from main.models import Category


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class TopWorkerViewSet(viewsets.ModelViewSet):
    queryset = TopWorker.objects.all()
    serializer_class = TopWorkerSerializer

class StatisticsViewSet(viewsets.ModelViewSet):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer