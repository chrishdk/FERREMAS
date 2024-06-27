from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer
from .services import created_category


class CategoryListView(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

class CategoryCreateView(APIView):
    def post(self, request):
            category = request.data.get('category')
            success, message = created_category(category)
            if success:
                return Response({"message": message}, status=status.HTTP_201_CREATED)
            else:
                return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST) 