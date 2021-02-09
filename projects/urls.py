from django.urls import path
from . import views

urlpatterns = [
    path("", views.project_index, name="project_index"),
    path("<int:pk>/", views.project_detail, name="project_detail"),
    path('contact_page/', views.contact_page, name='contact_page'),
    path('contact/', views.contact, name='contact'),
    path('abc/', views.test_html, name='abc')
]