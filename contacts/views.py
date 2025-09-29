from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer

class ContactCreate(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()
            ip = request.META.get("HTTP_X_FORWARDED_FOR") or request.META.get("REMOTE_ADDR")
            contact.ip_address = ip
            contact.save(update_fields=["ip_address"])
            return Response({"detail": "Mensaje recibido"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
