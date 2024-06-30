from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Branch
from .serializers import BranchSerializer

class BranchListView(APIView):
    def get(self, request):
        branches = Branch.objects.all()
        serializer = BranchSerializer(branches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AddBranchView(APIView):
    def post(self, request):
        serializer = BranchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BranchDetailView(APIView):
    def get(self, request, pk):
        try:
            branch = Branch.objects.get(pk=pk)
            serializer = BranchSerializer(branch)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Branch.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)