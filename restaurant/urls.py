from django.urls import path
from .views import PostListView
from . import views





urlpatterns = [

    path('', PostListView.as_view(),name = 'review-home'),
    path('about/', views.about,name = 'review-about'),
    path('review/<int:ID>/', views.restReviews, name='rest_reviews')

   
]
 