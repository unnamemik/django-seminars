"""
URL configuration for django_seminars project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from seminar6 import views

urlpatterns = [
    path('', views.seminar6, name='seminar6'),
    path('db/', views.total_in_db, name='total_in_db'),
    path('view/', views.total_in_view, name='total_in_view'),
    path('template/', views.total_in_template, name='total_in_template'),
]

