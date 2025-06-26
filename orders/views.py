from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import OrderSerializer,OrderItemSerializer
from .models import Order,OrderItem
from django.db import transaction
from products.models import Products


class AddOrder(APIView):
    def post(self, request):
        try:
            with transaction.atomic():
                order_data = request.data
                items_data = order_data.pop('items', [])


            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                order = serializer.save()

                for item in items_data:
                    product_id = item.get('product')
                    quantity = item.get('quantity')

                    try:
                        product = Products.objects.get(id=product_id)
                    except Products.DoesNotExist:
                        return Response({'error':f"Product with id {product_id} does not exist"},status=status.HTTP_400_BAD_REQUEST)

                    if product.stock < quantity:
                        return Response({'error':f'Insufficient stock for product {product.name}'})

                    product.stock -= quantity
                    product.save()

                    # Create OrderItem
                    OrderItem.objects.create(
                        order=order,
                        product=product,
                        quantity=quantity
                    )

                return Response({'message':'Your order has been added'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetOrder(APIView):
    def get(self,request):
        try:
            order = Order.objects.all()
            serializer = OrderSerializer(order, many=True)
            return Response({'message':'This are all the orders','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleOrder(APIView):
    def get(self,request,order_id):
        try:
            order = Order.objects.get(id=order_id)
            serializer = OrderSerializer(order)
            return Response({'message':'This is the order for this','data':serializer.data},status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditOrder(APIView):
    def put(self,request,order_id):
        try:
            order = Order.objects.get(id=order_id)
            serializer = OrderSerializer(order,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'This is order has been edited'},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteOrder(APIView):
    def delete(self,request,order_id):
        try:
            order = Order.objects.get(id=order_id)
            order.delete()
            return Response({'message':'This order has been deleted'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
