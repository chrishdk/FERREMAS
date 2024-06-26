from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart
from .serializers import CartSerializer
from .services import add_to_cart, remove_from_cart


class GetCartView(APIView):
    def get(self, request, cart_id):
        try:
            cart = Cart.objects.get(id=cart_id)
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Cart.DoesNotExist:
            return Response({"message": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)


# class AddToCartView(APIView):
#     def post(self, request):
#         cart_id = request.data.get('cart_id')
#         product_id = request.data.get('product_id')
#         branch_id = request.data.get('branch_id')
#         quantity = request.data.get('quantity')

#         try:
#             cart = Cart.objects.get(id=cart_id)
#         except Cart.DoesNotExist:
#             cart = Cart.objects.create()

#         success, message = add_to_cart(cart, product_id, branch_id, quantity)
#         if success:
#             serializer = CartSerializer(cart)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)


class RemoveFromCartView(APIView):
    def post(self, request):
        cart_id = request.data.get('cart_id')
        product_id = request.data.get('product_id')
        branch_id = request.data.get('branch_id')
        quantity = request.data.get('quantity')

        try:
            cart = Cart.objects.get(id=cart_id)
        except Cart.DoesNotExist:
            return Response({"message": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

        success, message = remove_from_cart(cart, product_id, branch_id, quantity)
        if success:
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)

class AddToCartView(APIView):
    def post(self, request):
        user = request.data.get('user')
        product_id = request.data.get('product_id')
        branch_id = request.data.get('branch_id')
        quantity = request.data.get('quantity')

        success, message = add_to_cart(user, product_id, branch_id, quantity)
        if success:
            cart = Cart.objects.get(user=user)
            serializer = CartSerializer(cart)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"message": message}, status=status.HTTP_400_BAD_REQUEST)