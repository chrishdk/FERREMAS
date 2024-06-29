from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, ProductWithPriceSerializer
from .services import get_products, create_product, get_products_with_latest_prices, product_deactivate, product_activate

class ProductListView(APIView):
    """
    Endpoint para obtener todos los productos activos.
    """
    def get(self, request):
        products = get_products()
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


class ProductActiveListView(APIView):
    def get(self, request):
        try:
            products = get_products_with_latest_prices()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response({"message": "Error fetching products"}, status=status.HTTP_400_BAD_REQUEST)
    

class ProductDeactivateView(APIView):
    def post(self, request):
        name = request.data.get('name')
        success, message = product_deactivate(name)
        if success:
            return Response({"message": message}, status=status.HTTP_200_OK)
        else:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)
        
        
class ProductActivateView(APIView):
    def post(self, request):
        name = request.data.get('name')
        success, message = product_activate(name)
        if success:
            return Response({"message": message}, status=status.HTTP_200_OK)
        else:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)