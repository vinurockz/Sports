from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from Sportsadmin.models import MyUser,Item_Creation_Model,Order_items_Model,CartModel
from  django.views.generic import TemplateView
from  .forms import Reg_Form,Log_Form

def homepage(request):
    return render(request,"main.html")


                                                                        # customer Register
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

                                                                                    # customer Login
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

                                                                        #list all sports items
class ListSports_View(TemplateView):
    template_name ="llistall.html"
    context={}

    def get(self,req,*args,**kwargs):
        sports=Item_Creation_Model.objects.all()
        self.context["sports"]=sports
        return render(req,self.template_name,self.context)

                                                                                    #Cart items
class SportsCart(TemplateView):
    model=CartModel
    template_name = "gotocart.html"
    context={}


    def get(self,req,*args,**kwargs):
        cart=self.model.objects.filter(status="cart")

        self.context["spitem"]=cart
        return render(req,self.template_name,self.context)

class AddtoSportsCart(TemplateView):
    model=CartModel
    def get(self,req,*args,**kwargs):
        pid=kwargs.get("id")
        sports=Item_Creation_Model.objects.get(id=pid)
        user=req.user
        cart=CartModel(product=sports,user=user)
        cart.save()
        return redirect("carted")