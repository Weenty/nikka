from django.urls import path

from main.views import CommentsView
from .views import *
urlpatterns = [
    path('sections/<int:pk>/', SectionsList.as_view()),
    path('categorys/', CategorysList.as_view()),
    path('categorys/<int:pk>/', CategorysList.as_view()),
    path('sections/', SectionsList.as_view()),
    path('products/', Products.as_view()),
    path('products/<int:product_id>', Products.as_view()),
    path('comments/<int:product_id>', CommentsView.as_view())
]
