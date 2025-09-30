from django.urls import path
from . import views

urlpatterns = [
    path('faqs/', views.FAQListCreateView.as_view(), name='faq-list'),
]
