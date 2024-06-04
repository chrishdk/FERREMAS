from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from .services import finalize_order

class FinalizeOrderView(APIView):
    def post(self, request):
        cart_id = request.data.get('cart_id')
        
        try:
            order = finalize_order(cart_id)
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except ValueError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
