from django.urls import path
from .views import AddReview,GetReview,SingleReview,EditReview,DeleteReview

urlpatterns = [
    path('add_review/',AddReview.as_view(),name='add_review'),
    path('get_review/',GetReview.as_view(),name='get_review'),
    path('single_review/<int:review_id>',SingleReview.as_view(),name='single_review'),
    path('edit_review/<int:review_id>',EditReview.as_view(),name='edit_review'),
    path('delete_review/<int:review_id>',DeleteReview.as_view(),name='delete_review')
]