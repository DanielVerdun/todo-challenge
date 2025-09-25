from django.urls import path
from users import views


"""
    Para utilizar las funciones de CreateUserView y RetreiveUpdateUserView hay que
    descomentar las lineas 12 y 14. Por el momento no se encuentran funcionales.
"""


urlpatterns = [
    #path('create/', views.CreateUserView.as_view()),
    path('token/', views.CreateTokenView.as_view()),
    #path('user/', views.RetreiveUpdateUserView.as_view()),
]