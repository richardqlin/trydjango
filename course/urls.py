from django.urls import path

from .view import (

	CourseView,

	)

	app_name = 'course'

	urlpatterns = [

	path('',CourseView.as_view(template_name='course.html'), name = 'course-list'),

	path('<int:id>/' , CourseView.as_view(), name = "course-detail"),


	]