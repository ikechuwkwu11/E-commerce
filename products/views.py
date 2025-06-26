from rest_framework import status
from rest_framework.response import Response
from .serializers import ProductsSerializer
from .models import Products
from rest_framework.views import APIView

class AddProduct(APIView):
    def post(self,request):
        try:
            serializer = ProductsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Your product has been added'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetProduct(APIView):
    def get(self,request):
        try:
            product = Products.objects.all()
            serializer = ProductsSerializer(product, many= True)
            return Response({'message':'This are all the products sold','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleProduct(APIView):
    def get(self,request,product_id):
        try:
            product = Products.objects.get(id=product_id)
            serializer = ProductsSerializer(product)
            return Response({'message':'This is the product','data':serializer.data},status=status.HTTP_200_OK)
        except Products.DoesNotExist:
            return Response({'message':'This product does not exist'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditProduct(APIView):
    def put(self,request,product_id):
        try:
            product = Products.objects.get(id=product_id)
            serializer = ProductsSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Your product has been edited'},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Products.DoesNotExist:
            return Response({'message':'This product does not exist'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteProduct(APIView):
    def delete(self,request,product_id):
        try:
            product = Products.objects.get(id=product_id)
            product.delete()
            return Response({'message':'Your product has been deleted'},status=status.HTTP_200_OK)
        except Products.DoesNotExist:
            return Response({'message':'This product does not exist'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


