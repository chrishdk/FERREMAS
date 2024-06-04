from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer

class TotalStockView(APIView):
    def get(self, request):
        # Obtiene el stock total de todos los productos en todas las sucursales
        total_stock = Stock.objects.all()
        serializer = StockSerializer(total_stock, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class BranchStockView(APIView):
    def get(self, request, branch_id):
        # Obtiene el stock por sucursal utilizando el ID de la sucursal
        branch_stock = Stock.objects.filter(branch_id=branch_id)
        serializer = StockSerializer(branch_stock, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class AddStockToBranchView(APIView):
    def post(self, request):
        product_id = request.data.get('product')
        branch_id = request.data.get('branch')
        quantity = request.data.get('quantity')

        try:
            # Verifica si ya existe un registro de stock para este producto y sucursal
            stock = Stock.objects.get(product_id=product_id, branch_id=branch_id)
            # Actualiza la cantidad en el stock existente
            stock.quantity += int(quantity)
            stock.save()
            serializer = StockSerializer(stock)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Stock.DoesNotExist:
            # Crea un nuevo registro de stock si no existe uno
            serializer = StockSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)