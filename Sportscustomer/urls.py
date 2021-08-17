from django.urls import path
from .views import Registration_View,Log_view,ListSports_View,SportsCart,AddtoSportsCart


urlpatterns = [

    path("regcust",Registration_View.as_view(),name="regcusted"),
    path("logcust",Log_view.as_view(),name="logcusted"),
    path("listing",ListSports_View.as_view(),name="listings"),



    #order
    path("cart",SportsCart.as_view(),name="carted"),
    path("addcart/<int:id>",AddtoSportsCart.as_view(),name="addedcart"),
]
