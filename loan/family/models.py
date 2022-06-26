from pickle import FALSE
from secrets import choice
from tabnanny import verbose
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Sandogh(models.Model):
     sandogh = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="مدیر")
     name = models.CharField(max_length=60 , blank= False ,verbose_name="نام صندوق")
     saham = models.IntegerField( blank= False , verbose_name="تعداد سهام")
     m_saham = models.IntegerField(blank=False , verbose_name= 'مبلغ هر سهم ')
     m_sandogh = models.IntegerField(blank=False , verbose_name= 'موجودی صندوق ')
     shomare_hesab =models.IntegerField(blank=False , verbose_name="شماره حساب")
     rolls = models.TextField(max_length=10000 , blank=True , verbose_name="توضیحات و قوانین")
     date_created = models.DateField(auto_now_add=True , verbose_name="تاریخ ایجاد صندوق")
     time = models.DateTimeField(auto_created= True ,auto_now_add=True,null=True ,verbose_name="زمان ایجاد صندوق")

     def __str__(self):
          return self.name

     def get_absolute_url(self):
          return reverse('family:dashbord' )     


class MemberManger(models.Manager):
     def state (self):
          return self.filter(status="وام نگرفته")
class Member(models.Model):
     status=models.CharField(max_length=10,choices=(('وام گرفته','وام گرفته'),('وام نگرفته','وام نگرفته')),default='وام نگرفته',verbose_name="وضعیت")
     membership=models.ForeignKey(Sandogh, on_delete=models.CASCADE , verbose_name="صندوق")
     author=models.ForeignKey(User, on_delete=models.CASCADE , verbose_name="مدیر")
     name= models.CharField(max_length=50, blank=False , verbose_name="نام")
     family=models.CharField(max_length=100, blank=True , verbose_name="نام خانوادگی")
     phone = models.IntegerField( blank=True  , verbose_name="شماره تلفن")
     t_saham =models.IntegerField( blank=False , verbose_name="تعداد سهام")
     created = models.DateField(auto_now_add=True, auto_created=True , verbose_name="تاریخ ایجاد")

     objects = MemberManger()

     class Meta :
          verbose_name ='اعضا'


     def get_absolute_url(self):
          return reverse('family:create')


     def __str__(self):
          return self.name 

class Loan(models.Model):
     STATUS_CHOICES = (
          ('پرداخت شده', 'پرداخت شده'),
          ('پرداخت نشده', 'پرداخت نشده'),
          ('در حال پرداخت', 'در حال پرداخت'),
          ('در انتظار پرداخت', 'در انتظار پرداخت'),
     )
     sandogh = models.ForeignKey(Sandogh,  on_delete=models.CASCADE , verbose_name="صندوق")
     author = models.ForeignKey(User, on_delete=models.CASCADE , verbose_name="مدیر")
     name = models.CharField(max_length=15 , blank=True , verbose_name="نام وام")
     m_vam = models.IntegerField(blank=False , verbose_name="مبلغ وام")
     m_ghest = models.IntegerField(blank=False , verbose_name="مبلغ قسط")
     t_gest = models.IntegerField(blank=False , verbose_name="تعداد قسط")
     choice = models.CharField(max_length=30, choices=STATUS_CHOICES, default='در انتظار پرداخت', verbose_name="وضعیت")
     created = models.DateField(auto_now_add=True, auto_created=True , verbose_name="تاریخ ایجاد")

     class Meta :
          verbose_name ='وام ها'


     def __str__(self):
          return self.name
   
     def get_absolute_url(self):
          return reverse('family:vam_list' )

class Lottory(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE , verbose_name="نام وام" )
    name = models.CharField(max_length=50, blank=False , verbose_name="نام")
    family = models.CharField(max_length=100, blank=False , verbose_name="نام خانوادگی")
    created = models.DateField(auto_now_add=True, auto_created=True , verbose_name="تاریخ ایجاد")


    class Meta :
          verbose_name ='برنده ها'

    def __str__(self):
          return  self.name
     
    def get_absolute_url(self):
          return reverse('family:vam_list' , kwargs={'pk':self.pk})      