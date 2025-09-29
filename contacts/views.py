from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer

class ContactCreateView(generics.ListCreateAPIView):
    queryset = Contact.objects.all().order_by("-created_at")
    serializer_class = ContactSerializer
