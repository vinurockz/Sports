from django.urls import path
from .views import homepage,Registration_View,Log_view,CreateSportsItem_View,ListSportsItem_View
from .views import CreateSportsItem_View,ListSportsItem_View,UpdateSportsItem_View,DeleteSportsItem_View
from .views import CreateProduct_View,ListProduct_View,UpdateProduct_View,DeleteProduct_View
urlpatterns = [
    #main events
    path("home",homepage,name="home"),
    path("reg",Registration_View.as_view(),name="reged"),
    path("log",Log_view.as_view(),name="loged"),


    #sports Items
    path("createsp",CreateSportsItem_View.as_view(),name="createsped"),
    path("listsp",ListSportsItem_View.as_view(),name="listsped"),
    path("updatesp/<int:pk>",UpdateSportsItem_View.as_view(),name="updatesped"),
    path("<pk>/deletesp",DeleteSportsItem_View.as_view(),name="deletesped"),


    #product Item
    path("createpr",CreateProduct_View.as_view(),name="createpred"),
    path("listpr",ListProduct_View.as_view(),name="listpred"),
    path("updatepr/<int:pk>",UpdateProduct_View.as_view(),name="updatepred"),
    path("<pk>/deletepr",DeleteProduct_View.as_view(),name="deletepred"),





]
