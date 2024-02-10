from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from django.contrib.auth import authenticate
from django.shortcuts import render, get_object_or_404

from . models import Income, IncomeCategory, Expense, ExpenseCategory, Asset, AssetCategory, Liability, LiabilityCategory
from . serializers import IncomeCategorySerializer, IncomeSerializer,ExpenseSerializer,AssetSerializer, LiabilitySerializer, ExpenseCategorySerializer, AssetCategorySerializer, LiabilityCategorySerializer


class IncomeCategoryView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return IncomeCategory.objects.all()
    
    def get_serializer_class(self):
        return IncomeCategorySerializer



class IncomeCategoryDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return IncomeCategory.objects.filter(id=pk)
    
    def get_serializer_class(self):
        return IncomeCategorySerializer



class IncomeView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Income.objects.filter(user_id=self.request.user.id)
    
    def get_serializer_class(self):
        return IncomeSerializer
    


class IncomeDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Income.objects.filter(user_id=self.request.user.id).filter(id=pk)
    
    def get_serializer_class(self):
        return IncomeSerializer
    
#######

class ExpenseCategoryView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ExpenseCategory.objects.all()
    
    def get_serializer_class(self):
        return ExpenseCategorySerializer



class ExpenseCategoryDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return ExpenseCategory.objects.filter(id=pk)
    
    def get_serializer_class(self):
        return ExpenseCategorySerializer



class ExpenseView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Expense.objects.filter(user_id=self.request.user.id)
    
    def get_serializer_class(self):
        return ExpenseSerializer
    


class ExpenseDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Expense.objects.filter(user_id=self.request.user.id).filter(id=pk)
    
    def get_serializer_class(self):
        return ExpenseSerializer
    
#######

class AssetCategoryView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return AssetCategory.objects.all()
    
    def get_serializer_class(self):
        return AssetCategorySerializer



class AssetCategoryDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return AssetCategory.objects.filter(id=pk)
    
    def get_serializer_class(self):
        return AssetCategorySerializer



class AssetView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Asset.objects.filter(user_id=self.request.user.id)
    
    def get_serializer_class(self):
        return AssetSerializer
    


class AssetDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Asset.objects.filter(user_id=self.request.user.id).filter(id=pk)
    
    def get_serializer_class(self):
        return AssetSerializer
    
#######

class LiabilityCategoryView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LiabilityCategory.objects.all()
    
    def get_serializer_class(self):
        return LiabilityCategorySerializer



class LiabilityCategoryDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return LiabilityCategory.objects.filter(id=pk)
    
    def get_serializer_class(self):
        return LiabilityCategorySerializer



class LiabilityView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Liability.objects.filter(user_id=self.request.user.id)
    
    def get_serializer_class(self):
        return LiabilitySerializer
    


class LiabilityDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Liability.objects.filter(user_id=self.request.user.id).filter(id=pk)
    
    def get_serializer_class(self):
        return LiabilitySerializer