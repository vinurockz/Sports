from django.shortcuts import render,redirect
from django.urls import reverse_lazy

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

class SportsDetail(TemplateView):
    model = Item_Creation_Model
    template_name = "sportslist.html"
    context = {}

    def get(self, req, *args, **kwargs):
        id = kwargs.get("pk")
        sport = self.model.objects.get(id=id)
        self.context["sport"] = sport
        return render(req, self.template_name, self.context)
                                                                            # Sports Item Update
class UpdateSportsItem_View(UpdateView):
    model = Item_Creation_Model
    template_name = "itemcreate/updatesp.html"
    form_class = CreateSportItems_Form
    success_url = reverse_lazy('listsped')
                                                                                # Sports Item Delete
class DeleteSportsItem_View(DeleteView):
    model = Item_Creation_Model
    template_name = "itemcreate/deleteview.html"
    success_url = reverse_lazy('listsped')
    context_object_name = "sportsd"

                                                                                # product Create
class CreateProduct_View(CreateView):
    model = Product_Model
    form_class =ProductName_Form
    template_name = "product/createproduct.html"
    success_url = "listpr"
    context = {}

                                                                                     # product List
class ListProduct_View(ListView):
    model = Product_Model
    template_name = "product/listpr.html"
    context_object_name = "product"

                                                                                # product Update
class UpdateProduct_View(UpdateView):
    model = Product_Model
    template_name = "product/updatepr.html"
    form_class = ProductName_Form
    success_url = reverse_lazy('listpred')

                                                                        # product Delete
class DeleteProduct_View(DeleteView):
    model = Product_Model
    template_name = "product/deletepr.html"
    success_url = reverse_lazy('listpred')
    context_object_name = "productd"
                                                                            # Catagory Create
class CreateCatagory_View(CreateView):
    model = Sports_Catagory_Model
    form_class =SportsCategory_Form
    template_name = "sports_catagory/createsc.html"
    success_url = "listsc"
    context = {}

                                                                                     # Catagory List
class ListCatagory_View(ListView):
    model = Sports_Catagory_Model
    template_name = "sports_catagory/listsc.html"
    context_object_name = "catagory"

                                                                                # Catagory Update
class UpdateCatagory_View(UpdateView):
    model = Sports_Catagory_Model
    template_name = "sports_catagory/updatesc.html"
    form_class = SportsCategory_Form
    success_url = reverse_lazy('listsced')

                                                                        # Catagory Delete
class DeleteCatagory_View(DeleteView):
    model = Sports_Catagory_Model
    template_name = "sports_catagory/deletesc.html"
    success_url = reverse_lazy('listsced')
    context_object_name = "catagoryd"









