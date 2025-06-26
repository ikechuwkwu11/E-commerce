from django.core.serializers import serialize
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import VendorsSerializer
from .models import Vendors

class AddVendor(APIView):
    def post(self,request):
        try:
            serializer = VendorsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully added a vendor'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetVendor(APIView):
    def get(self,request):
        try:
            vendor = Vendors.objects.all()
            serializer = VendorsSerializer(vendor, many=True)
            return Response({'message':'This are all the vendors','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleVendor(APIView):
    def get(self,request,vendor_id):
        try:
            vendor = Vendors.objects.get(id = vendor_id)
            serializer = VendorsSerializer(vendor)
            return Response({'message':'This is a vendor profile','data':serializer.data},status=status.HTTP_200_OK)
        except Vendors.DoesNotExist:
            return Response({'message':'This vendor does not exist'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditVendor(APIView):
    def put(self,request,vendor_id):
        try:
            vendor = Vendors.objects.get(id = vendor_id)
            serializer = VendorsSerializer(vendor, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Your vendor has been edited'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteVendor(APIView):
    def delete(self,request,vendor_id):
        try:
            vendor = Vendors.objects.get(id = vendor_id)
            vendor.delete()
            return Response({'message':'This vendor has been deleted'},status=status.HTTP_200_OK)
        except Vendors.DoesNotExist:
            return Response({'message':'This vendor does not exist here!'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
