from django.shortcuts import render
from rest_framework.views import APIView
from .models import Persona
from .serializers import PersonaSerializer
from rest_framework.response import Response

class PersonaList(APIView):
    def get(self, request):
        personas = Persona.objects.all()
        serializer = PersonaSerializer(personas, many=True)
        return Response(serializer.data)


