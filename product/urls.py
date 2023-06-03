from django.urls import path

from . import views

urlpatterns = [
    path('category/<str:pk>', views.ProductCategoryList.as_view()),
    path('desc/<str:pk>', views.ProductDescription.as_view()),
]
