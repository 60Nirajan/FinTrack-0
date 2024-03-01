# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveUpdateAPIView

from django.shortcuts import get_object_or_404
from django.db.models import Sum

from datetime import datetime, date

from . models import User, Income, IncomeCategory, Expense, ExpenseCategory, Asset,\
                    AssetCategory, Liability, LiabilityCategory, TargetWallet, Target
from . serializers import IncomeCategorySerializer, IncomeSerializer,ExpenseSerializer,\
                            AssetSerializer, LiabilitySerializer, ExpenseCategorySerializer,\
                            AssetCategorySerializer, LiabilityCategorySerializer, \
                            TargetWalletSerializer, TargetSerializer

#######

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
    

#######

class TotalIncomeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_income = Income.objects.filter(user_id=self.request.user.id).aggregate(total_income=Sum('income_amount'))
        return Response(total_income)
    


class TotalExpenseView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_income = Income.objects.filter(user_id=self.request.user.id).aggregate(total_income=Sum('income_amount'))
        total_expense = Expense.objects.filter(user_id=self.request.user.id).aggregate(total_expense=Sum('expense_amount'))
        expense_notification =''
        if total_income['total_income'] < total_expense['total_expense']:
            expense_notification = "Expense exceeded Income"
        elif total_expense['total_expense'] > 100000:
            expense_notification = "Expense More than Threshold"
        return Response({"total_expense": total_expense['total_expense'], "expense_notification":expense_notification})
    


class TotalAssetView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_asset = Asset.objects.filter(user_id=self.request.user.id).aggregate(total_asset=Sum('asset_amount'))
        return Response(total_asset)
    


class TotalLiabilityView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_liability = Liability.objects.filter(user_id=self.request.user.id).aggregate(total_liability=Sum('liability_amount'))
        return Response(total_liability)

#####

class BalanceView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        total_income = Income.objects.filter(user_id=self.request.user.id).aggregate(total_income=Sum('income_amount'))['total_income']
        total_expense = Expense.objects.filter(user_id=self.request.user.id).aggregate(total_expense=Sum('expense_amount'))['total_expense']
        return Response({"balance_amount":total_income-total_expense})
    

#####
    
class HistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        income_history = Income.objects.filter(user=request.user).values('income_amount', 'income_note', 'income_date')
        expense_history = Expense.objects.filter(user=request.user).values('expense_amount', 'expense_note', 'expense_date')
        liability_history = Liability.objects.filter(user=request.user).values('liability_amount', 'liability_note', 'liability_date')
        asset_history = Asset.objects.filter(user=request.user).values('asset_amount', 'asset_note', 'asset_date')
        combined_history = list(income_history) + list(expense_history) + list(liability_history) + list(asset_history)
        combined_history_sorted = sorted(combined_history, key=lambda x: x.get('income_date', 
                                         x.get('expense_date', 
                                         x.get('liability_date', 
                                         x.get('asset_date', datetime.min)))), reverse=True)
        return Response(combined_history_sorted)
    
########
    
class TargetWalletCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return TargetWallet.objects.filter(user_id=self.request.user.id)
    
    def get_serializer_class(self):
        return TargetWalletSerializer



class TargetWalletDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, index):
        target_wallet = TargetWallet.objects.get(user_id=request.user.id)
        if index == "update":
            target_wallet.amount = request.data['amount']
        elif index == "add":
            target_wallet.amount += request.data['amount']
        target_wallet.save()
        
        user = User.objects.get(id=request.user.id)
        self.function_start(user)

        return Response({"detail":"success update"}, status=status.HTTP_201_CREATED)

    def function_start(self, user):
        target_wallet_queryset = TargetWallet.objects.get(user_id=user.id)
        total_wallet = target_wallet_queryset.amount
        targets = Target.objects.filter(user_id=user.id).filter(target_status='INCP').filter(target_deadline__gt=date.today())
        
        total_priority = 0
        for target in targets:
            if target.target_priority == "H":
                total_priority += 0.5
            elif target.target_priority == "M":
                total_priority += 0.3
            else:
                total_priority += 0.2

        for target in targets:
            float_target_priority = 0
            if target.target_priority == "H":
                float_target_priority = 0.5
            elif target.target_priority == "M":
                float_target_priority = 0.3
            else:
                float_target_priority = 0.2
            target_divided_amount = (total_wallet / total_priority) * float_target_priority

            if target.target_amount > target_divided_amount:
                target.current_amount = target_divided_amount
                target.save()
            
            else:
                target.current_amount = target.target_amount
                target.target_status = "COMP"
                target_wallet_queryset.amount -= target.target_amount
                target.save()
                target_wallet_queryset.save()
                # Recursion
                self.function_start(user)
                break
    


class TargetListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Target.objects.filter(user_id=self.request.user.id)
    
    def get_serializer_class(self):
        return TargetSerializer



class TargetDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Target.objects.filter(user_id=self.request.user.id).filter(id=pk)
    
    def get_serializer_class(self):
        return TargetSerializer
    