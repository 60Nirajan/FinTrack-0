from django.urls import path

from . import views

urlpatterns = [
    path('incomecategories/<int:pk>/', views.IncomeCategoryDetailView.as_view()),
    path('incomecategories/', views.IncomeCategoryView.as_view()),
    path('incomes/', views.IncomeView.as_view()),
    path('incomes/<int:pk>/', views.IncomeDetailView.as_view()),

    path('expensecategories/<int:pk>/', views.ExpenseCategoryDetailView.as_view()),
    path('expensecategories/', views.ExpenseCategoryView.as_view()),
    path('expenses/', views.ExpenseView.as_view()),
    path('expenses/<int:pk>/', views.ExpenseDetailView.as_view()),

    path('assetcategories/<int:pk>/', views.AssetCategoryDetailView.as_view()),
    path('assetcategories/', views.AssetCategoryView.as_view()),
    path('assets/', views.AssetView.as_view()),
    path('assets/<int:pk>/', views.AssetDetailView.as_view()),
    
    path('liabilitycategories/<int:pk>/', views.LiabilityCategoryDetailView.as_view()),
    path('liabilitycategories/', views.LiabilityCategoryView.as_view()),
    path('liabilitys/', views.LiabilityView.as_view()),
    path('liabilitys/<int:pk>/', views.LiabilityDetailView.as_view()),

]
