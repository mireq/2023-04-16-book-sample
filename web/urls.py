# -*- coding: utf-8 -*-
from . import views
from django.urls import path


urlpatterns = [
	path('rs/', views.RatingStandardView.as_view(), name='rs'),
	path('rc/', views.RatingCursorView.as_view(), name='rc'),
]
