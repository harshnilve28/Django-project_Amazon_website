from django.urls import path
from Clothes import views

urlpatterns = [
    path("", views.home, name="home"),  # Home page
    path("update/<int:id>/", views.update_data, name="update_product"),  # Update product
    path("delete/<int:id>/", views.delete_data, name="delete_product"),  # Delete product
]
