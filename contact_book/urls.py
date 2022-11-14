"""lcs_pcom7e_september_2022 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""

from django.urls import path

from contact_book import views

urlpatterns = [
    path("create", views.create, ),
    path("update/<int:index>", views.update_by_id, ),
    path("delete/<int:index>", views.delete_by_id, ),
    path("delete-all", views.delete_all, ),
    path("get/<int:index>", views.get_by_id, ),
    path("", views.list_all, name="index"),
]
