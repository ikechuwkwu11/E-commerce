from django.core.serializers import serialize
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import ReviewSerializer
from .models import Review

class AddReview(APIView):
    def post(self,request):
        try:
            serializer = ReviewSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Your review has been gotten'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetReview(APIView):
    def get(self,request):
        try:
            review = Review.objects.all()
            serializer = ReviewSerializer(review, many=True)
            return Response({'message':'This are all the reviews','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error', 'error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleReview(APIView):
    def get(self,request,review_id):
        try:
            review = Review.objects.get(id= review_id)
            serializer = ReviewSerializer(review)
            return Response({'message':'This is this particular review','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditReview(APIView):
    def put(self,request,review_id):
        try:
            review = Review.objects.get(id=review_id)
            serializer = ReviewSerializer(review, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Your review has been edited'},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Review.DoesNotExist:
            return Response({'message':'This Review does not exist'},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteReview(APIView):
    def delete(self,request,review_id):
        try:
            review = Review.objects.get(id=review_id)
            review.delete()
            return Response({'message':'You have successfully deleted the review'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
