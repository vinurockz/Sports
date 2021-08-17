from django.urls import path
from .views import homepage,Registration_View,Log_view
from .views import SportsDetail
from .views import CreateSportsItem_View,ListSportsItem_View,UpdateSportsItem_View,DeleteSportsItem_View
from .views import CreateProduct_View,ListProduct_View,UpdateProduct_View,DeleteProduct_View
from .views import CreateCatagory_View,ListCatagory_View,UpdateCatagory_View,DeleteCatagory_View
urlpatterns = [
    #main events
    path("home",homepage,name="home"),
    path("reg",Registration_View.as_view(),name="reged"),
    path("log",Log_view.as_view(),name="loged"),
    path("detail/<int:pk>",SportsDetail.as_view(),name="details"),


    #sports Items
    path("createsp",CreateSportsItem_View.as_view(),name="createsped"),
    path("listsp",ListSportsItem_View.as_view(),name="listsped"),
    path("updatesp/<int:pk>",UpdateSportsItem_View.as_view(),name="updatesped"),
    path("deletesp/<int:pk>",DeleteSportsItem_View.as_view(),name="deletesped"),


    #product Item
    path("createpr",CreateProduct_View.as_view(),name="createpred"),
    path("listpr",ListProduct_View.as_view(),name="listpred"),
    path("updatepr/<int:pk>",UpdateProduct_View.as_view(),name="updatepred"),
    path("deletepr/<int:pk>",DeleteProduct_View.as_view(),name="deletepred"),


    # sports_catagory Item
    path("createsc", CreateCatagory_View.as_view(), name="createsced"),
    path("listsc", ListCatagory_View.as_view(), name="listsced"),
    path("updatesc/<int:pk>", UpdateCatagory_View.as_view(), name="updatesced"),
    path("deletesc/<int:pk>", DeleteCatagory_View.as_view(), name="deletesced"),

]
