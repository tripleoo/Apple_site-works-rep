from django.urls import path

from . import views

urlpatterns = [
    path('', views.Glav.as_view(), name='glav'),
    path('iphone/<slug:devise_slug>', views.PageIphone.as_view(), name='iphone'),
    path('iphone/buy/<int:id>', views.Buy.as_view(), name='buy'),
    path('test/', views.test, name='test'),
    path('review/<int:iphone_id>/', views.AddReview.as_view(), name='review'),
    path('filter/<str:category_slug>/', views.Filter_By_Category.as_view(), name='filter_by_category'),
]

