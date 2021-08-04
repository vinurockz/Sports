from django.shortcuts import render,redirect
from .models import Item_Creation_Model,Sports_Catagory_Model,Product_Model,MyUser
from .forms import SportsCategory_Form,ProductName_Form,CreateSportItems_Form,Reg_Form,Log_Form
from  django.views.generic import TemplateView,CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth import authenticate,login,logout




# Create your views here.
def homepage(request):
    return render(request,"index.html")



class Registration_View(TemplateView):
    model=MyUser
    template_name ="reg.html"
    form_class=Reg_Form
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(self.request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("reged")


class Log_view(TemplateView):
    model=MyUser
    form_class=Log_Form
    template_name = "log.html"
    context={}
    def get(self,request,*args,**kwargs):
        form=self.form_class()
        self.context["form"]=form
        return render(self.request,self.template_name,self.context)
    def post(self,request,*args,**kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get("email")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=email,password=password)
            if(user):
                login(request,user)
                return redirect("home")
            else:
                form = self.form_class()
                self.context["form"] = form
                return redirect("loged")
                                                                        # Sports Item Create
class CreateSportsItem_View(CreateView):
    model = Item_Creation_Model
    form_class = CreateSportItems_Form
    template_name = "itemcreate/createsports.html"
    success_url = "listsp"
    context={}
                                                                        # Sports Item Listing
class ListSportsItem_View(ListView):
    model = Item_Creation_Model
    template_name = "itemcreate/listsp.html"
    context_object_name = "sports"
                                                                            # Sports Item Update
class UpdateSportsItem_View(UpdateView):
    model = Item_Creation_Model
    template_name = "itemcreate/updatepr.html"
    form_class = CreateSportItems_Form
    success_url = "listsp"
                                                                                # Sports Item Delete
class DeleteSportsItem_View(DeleteView):
    model = Item_Creation_Model
    template_name = "itemcreate/deleteview.html"
    success_url = "listsp"
    context_object_name = "sportsd"

                                                                                # product Create
class CreateProduct_View(CreateView):
    model = Product_Model
    form_class =ProductName_Form
    template_name = "product/createproduct.html"
    success_url = "listpr"
    context = {}


class ListProduct_View(ListView):
    model = ProductName_Form
    template_name = "product/listpr.html"
    context_object_name = "product"


class UpdateProduct_View(UpdateView):
    model = ProductName_Form
    template_name = "product/updatepr.html"
    form_class = CreateSportItems_Form
    success_url = "listpr"


class DeleteProduct_View(DeleteView):
    model = ProductName_Form
    template_name = "deleteview.html"
    success_url = "listpr"
    context_object_name = "productd"








