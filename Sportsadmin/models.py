from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models

# Create your models here.

class CricketItemsModel(models.Model):
    name_item=models.CharField(max_length=200)
    choice=(("bat","bat"),("ball","ball"),("helmet","helmet"),
            ("pad","pad"),("shoes","shoes"),("stumb","stumb"),
            ("fullkit","fullkit"),("cap","cap"),("glovse","glovse"),("jersy","jersy"),("select","select"))
    item_type=models.CharField(max_length=100,choices=choice,default="select")
    item_image=models.ImageField(upload_to="sports/cricket/")
    note=models.CharField(max_length=500)
    price=models.FloatField()
    warranty=models.CharField(max_length=100)
    Offer=models.CharField(max_length=50)
    count=models.IntegerField()

class FootballItemsModel(models.Model):
    name_item = models.CharField(max_length=200)
    choice = (("football", "football"), ("Goal Post", "Goal Post"),
              ("pad", "pad"), ("shoes", "shoes"),
              ("fullkit", "fullkit"), ("glovse", "glovse"), ("jersy", "jersy"), ("select", "select"))
    item_type = models.CharField(max_length=100, choices=choice, default="select")
    item_image = models.ImageField(upload_to="sports/football/")
    note = models.CharField(max_length=500)
    price = models.FloatField()
    warranty = models.CharField(max_length=100)
    Offer = models.CharField(max_length=50)
    count = models.IntegerField()

class BadmintonItemModel(models.Model):
    name_item = models.CharField(max_length=200)
    choice = (("bat", "bat"), ("ball", "ball"),("Badminton net", "Badminton net"),
              ("pad", "pad"), ("shoes", "shoes"), ("corke", "corke"),
              ("fullkit", "fullkit"), ("cap", "cap"), ("jersy", "jersy"), ("select", "select"))
    item_type = models.CharField(max_length=100, choices=choice, default="select")
    item_image = models.ImageField(upload_to="sports/badminton/")
    note = models.CharField(max_length=500)
    price = models.FloatField()
    warranty = models.CharField(max_length=100)
    Offer = models.CharField(max_length=50)
    count = models.IntegerField()

class CarromChessItemModel(models.Model):
    name_item = models.CharField(max_length=200)
    choice = (("chess board", "chess board"), ("carom board", "carom board"),("chess coins", "chess coins"),
              ("powder", "powder"), ("stricker", "stricker"), ("carom coins", "carom coins"),
              ("chess fullkit", "chess fullkit"), ("cap", "cap"), ("jersy", "jersy"), ("select", "select"),
    ("carom fullkit", "carom fullkit"))
    item_type = models.CharField(max_length=100, choices=choice, default="select")
    item_image = models.ImageField(upload_to="sports/caromchess/")
    note = models.CharField(max_length=500)
    price = models.FloatField()
    warranty = models.CharField(max_length=100)
    Offer = models.CharField(max_length=50)
    count = models.IntegerField()

class SportsItemModel(models.Model):
    cricket_item = models.ForeignKey(CricketItemsModel, on_delete=models.CASCADE)
    football_item = models.ForeignKey(FootballItemsModel, on_delete=models.CASCADE)
    badminton_item = models.ForeignKey(BadmintonItemModel, on_delete=models.CASCADE)
    carromchess_item = models.ForeignKey(CarromChessItemModel, on_delete=models.CASCADE)


class CartModel(models.Model):
    Items=models.ForeignKey(SportsItemModel,on_delete=models.CASCADE)
    user=models.CharField(max_length=130)
    date=models.DateField(auto_now=True)
    choice=(("cart","cart"),("order placed","orderplaced"),
            ("buyed","buyed"),("waiting user response","waiting user response"),
            ("canceled from cart","canceled from cart"))
    status_order=models.CharField(max_length=50,choices=choice,default="cart")

class Order_items_Model(models.Model):
    order_id=models.IntegerField()
    Order_Items=models.ForeignKey(SportsItemModel,on_delete=models.CASCADE)
    user=models.CharField(max_length=130)
    date=models.DateField(auto_now=True)
    address=models.CharField(max_length=300)
    pincode=models.CharField(max_length=6)
    phonenumber=models.CharField(max_length=10)
    choice = (("ordered", "ordered"), ("packed", "packed"), ("shipped", "shipped"),
               ("delivered", "delivered"), ("cancelled", "cancelled"))
    status_order=models.CharField(max_length=50,choices=choice,default="ordered")

class Compalaines_Model(models.Model):
    order=models.ForeignKey(Order_items_Model,on_delete=models.CASCADE)
    complaint_img=models.ImageField(upload_to="sports/complaints/")
    complaint_order=models.CharField(max_length=1000)

class Feedback_Model(models.Model):
    order=models.ForeignKey(Order_items_Model,on_delete=models.CASCADE)
    feedback_text=models.CharField(max_length=1000)
    choice=(("Fast delivered","Fast delivered"),("Exlant","Exlant"),("good","good"),("bad","bad"))



class MyUserManager(BaseUserManager):
    def create_user(self, email,user_name, phone_number, wallet_amount,password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name,
            phone_number=phone_number,
            wallet_amount=wallet_amount
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,user_name, phone_number,wallet_amount,password=None):

        user = self.create_user(
            email,
            user_name=user_name,
            password=password,
            phone_number=phone_number,
            wallet_amount=wallet_amount


        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    user_name=models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16,unique=True)
    wallet_amount=models.FloatField()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','phone_number','wallet_amount']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin








