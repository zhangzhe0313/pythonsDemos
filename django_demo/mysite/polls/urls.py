#!/usr/bin/enc python
# -*- coding: UTF-8 -*-

# @File: urls.py
# @Time: 2019-1-28 15:32

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]