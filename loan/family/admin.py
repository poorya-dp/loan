from dataclasses import fields
from re import S
from django.contrib import admin
from .models import Sandogh , Member , Loan , Lottory

# Register your models here.

class SandoghAdmin(admin.ModelAdmin):
    list_display =('name','saham','m_saham','shomare_hesab','rolls','date_created','time')
   
   
admin.site.register(Sandogh , SandoghAdmin)

class MemberAdmin(admin.ModelAdmin):
    list_display = ('membership','name','family','t_saham','phone','created')

admin.site.register(Member, MemberAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ('sandogh','name','m_vam','m_ghest','t_gest','choice','created')
admin.site.register(Loan, LoanAdmin)

class LottoryAdmin(admin.ModelAdmin):
    list_display = ('name','family','loan','created')
admin.site.register(Lottory, LottoryAdmin)

