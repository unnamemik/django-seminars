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

from django.urls import path
from seminar3 import views

urlpatterns = [
    path('', views.seminar3, name='seminar3'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('heads_tails/<int:n>/', views.heads_tails, name='heads_tails'),
    path('dice/<int:n>/', views.dice, name='dice'),
    path('rand/<int:n>/', views.rand, name='rand'),
    path('united/<int:n>/', views.united, name='united'),

    path('author/<int:author_id>/', views.author_posts, name='author_posts'),
    path('post/<int:post_id>/', views.post_full, name='post_full'),

    path('comment/<int:post_id>/', views.post_comm, name='post_comm'),

    path('basket/<int:user_id>/', views.basket, name='basket'),
    path('sorted_basket/<int:user_id>/<int:days_ago>/', views.sorted_basket, name='sorted_basket'),
]

