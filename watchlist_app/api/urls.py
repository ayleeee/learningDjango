
from django.urls import path,include
#from watchlist_app.api.views import movie_list,movie_details
from watchlist_app.api.views import (ReviewDetail, StreamPlatformDetailAV, StreamPlatformVS, 
                                     WatchDetailAV,WatchListAV,StreamPlatformAV,
                                     StreamPlatformDetailAV,ReviewList,ReviewCreate)

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('stream',StreamPlatformVS,basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list' ),
    path('<int:pk>', WatchDetailAV.as_view() ,name='movie-detail'),
    #path('stream/', StreamPlatformAV.as_view(), name='stream'),
    #path('stream/<int:pk>', StreamPlatformDetailAV.as_view(),name='stream-detail'),
    
    path('',include(router.urls)),
  
    # path('review/',ReviewList.as_view(),name='review-list'),
    
    # path('review/<int:pk>',ReviewDetail.as_view(),name='review-detail')
    
    # I need all the reviews from this particular movie
    path('stream/<int:pk>/review',ReviewList.as_view(),name='review-list'),
    path('stream/<int:pk>/review-create',ReviewCreate.as_view(),name='review-create'),
    path('stream/review/<int:pk>',ReviewDetail.as_view(),name='review-detail')
]
