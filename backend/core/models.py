from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator # input validation

# Create your models here.

class User(AbstractUser):
    phone_no = models.CharField(max_length=15, blank=True, null=True)


class IncomeCategory(models.Model):
    category_name = models.CharField(max_length  = 255) 

    def __str__(self):
        return f'{self.category_name}'


class Income(models.Model):
    income_note = models.CharField(max_length  = 255)
    income_amount = models.DecimalField(max_digits = 14, decimal_places = 2, validators = [MinValueValidator(1)])
    income_date = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    income_category = models.ForeignKey(IncomeCategory, on_delete = models.PROTECT)


class ExpenseCategory(models.Model):
    category_name = models.CharField(max_length  = 255)

    def __str__(self):
        return f'{self.category_name}'
    

class Expense(models.Model):
    expense_note = models.CharField(max_length  = 255)
    expense_amount = models.DecimalField(max_digits = 14, decimal_places = 2, validators = [MinValueValidator(1)])
    expense_date = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    expense_category = models.ForeignKey(ExpenseCategory, on_delete = models.PROTECT)


class AssetCategory(models.Model):
    category_name = models.CharField(max_length  = 255)

    def __str__(self):
        return f'{self.category_name}'


class Asset(models.Model):
    asset_note = models.CharField(max_length  = 255)
    asset_amount = models.DecimalField(max_digits = 14, decimal_places = 2, validators = [MinValueValidator(1)])
    asset_date = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    asset_category = models.ForeignKey(AssetCategory, on_delete = models.PROTECT)


class LiabilityCategory(models.Model):
    category_name = models.CharField(max_length  = 255)

    def __str__(self):
        return f'{self.category_name}'


class Liability(models.Model):
    liability_note = models.CharField(max_length  = 255)
    liability_amount = models.DecimalField(max_digits = 14, decimal_places = 2, validators = [MinValueValidator(1)])
    liability_date = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    liability_category = models.ForeignKey(LiabilityCategory, on_delete = models.PROTECT)
    

class Target(models.Model):
    target_name = models.CharField(max_length = 255)
    current_amount = models.FloatField()
    target_amount = models.FloatField()
    target_add_date = models.DateTimeField(auto_now = True)
    target_deadline = models.DateTimeField(auto_now = False)
    completed = 'COMP'
    incomplete = 'INCP'
    target_choices = [(completed, 'completed'),
                      (incomplete, 'incomplete')]
    target_status  = models.CharField(max_length =4, choices = target_choices, default = incomplete)
    low = 'L'
    medium = 'M'
    high = 'H'
    priority_choices = [(low, 'low'),
                      (medium, 'medium'),
                      (high, 'high')]
    target_priority = models.CharField(max_length = 1, choices = priority_choices)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.target_name}'


class TargetWallet(models.Model):
    amount = models.FloatField()
    user = models.OneToOneField(User, on_delete = models.CASCADE)
