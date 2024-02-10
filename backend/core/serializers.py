from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer, UserSerializer as BaseUserSerializer

from . models import IncomeCategory, Income,Expense,Asset,Liability,ExpenseCategory,AssetCategory,LiabilityCategory


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name','phone_no']



class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name','phone_no']



class IncomeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeCategory
        fields = ['id', 'category_name']



class IncomeSerializer(serializers.ModelSerializer):
    user_id = user_id = serializers.IntegerField()
    income_category_id = serializers.IntegerField()
    class Meta:
        model = Income
        fields = ['id', 'income_note', 'income_amount', 'income_date', 'user_id', 'income_category_id']



class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ['id', 'category_name']



class ExpenseSerializer(serializers.ModelSerializer):
    user_id = user_id = serializers.IntegerField()
    expense_category_id = serializers.IntegerField()
    class Meta:
        model = Income
        fields = ['id', 'expense_note', 'expense_amount', 'expense_date', 'user_id', 'expense_category_id']



class AssetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetCategory
        fields = ['id', 'category_name']



class AssetSerializer(serializers.ModelSerializer):
    user_id = user_id = serializers.IntegerField()
    asset_category_id = serializers.IntegerField()
    class Meta:
        model = Asset
        fields = ['id', 'asset_note', 'asset_amount', 'asset_date', 'user_id', 'asset_category_id']



class LiabilityCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LiabilityCategory
        fields = ['id', 'category_name']



class LiabilitySerializer(serializers.ModelSerializer):
    user_id = user_id = serializers.IntegerField()
    liability_category_id = serializers.IntegerField()
    class Meta:
        model = Liability
        fields = ['id', 'liability_note', 'liability_amount', 'liability_date', 'user_id', 'liability_category_id']


