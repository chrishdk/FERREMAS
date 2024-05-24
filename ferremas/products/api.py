from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .services import get_active_products, create_product

class ActiveProductListView(APIView):
    """
    Endpoint para obtener todos los productos activos.
    """
    def get(self, request):
        products = get_active_products()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class AddProductView(APIView):
    def post(self, request):
        name = request.data.get('name')
        description = request.data.get('description')
        price = request.data.get('price')
        success, message = create_product(name, description, price)
        if success:
            return Response({"message": message}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
