from django.urls import path
from pra_app import views

urlpatterns = [
	path('b', views.bye, name="bye"),
	path('', views.index, name="index"),
	path('contact/', views.form_view, name="form_view"),
    
]