from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect 
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .forms import SingUpForm, SandoghForm , LottoryForm
from .models import  Member , Sandogh ,Loan ,Lottory
from .mixins import FieldsMixin ,AuthorAccessMixin
import random


# Create your views here.


class IndexView(TemplateView):
    template_name = 'family/index.html'

    # sessions
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_visits'] = self.request.session['num_visits']
        return context

    def get(self, request, *args, **kwargs):
        num_visits = request.session.get('num_visits', 0)
        request.session['num_visits'] = num_visits + 1
        return super().get(request, *args, **kwargs)


def singup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            pass1 = form.cleaned_data.get('password1')
            pass2 = form.cleaned_data.get('password2')
            if pass1 == pass2:
                user = authenticate(username=username, password=pass1)
                login(request, user)
            return redirect('family:fund_create')

    else:
        form = SingUpForm()
    return render(request, 'family/singup.html', {'form': form})






class FundCreateView(CreateView ,LoginRequiredMixin):
    model = Sandogh
    template_name = 'family/sform.html'
    fields = '__all__'
    login_url = '/login/'

# list funds and updateview and delete view

class FundListView(generic.ListView , LoginRequiredMixin):
    model = Sandogh 
    context_object_name = 'fund_list'
    template_name = 'family/fundlist.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Sandogh.objects.all()
        else:
            return Sandogh.objects.filter(sandogh=self.request.user)

class FundUpdateView(UpdateView ,LoginRequiredMixin,AuthorAccessMixin ):
    model = Sandogh
    model_form = SandoghForm
    template_name = 'family/sform.html'
    fields = ('name' ,'saham','m_saham','m_sandogh','shomare_hesab')
    success_url = reverse_lazy('family:fund_list')


class FundDeleteView(DeleteView ,LoginRequiredMixin ,AuthorAccessMixin):
    model = Sandogh
    template_name = 'family/DeleteFund_form.html'
    success_url = reverse_lazy('family:fund_list')


# memeber create view uodate view delete view
class MemberCreate(CreateView ,LoginRequiredMixin , FieldsMixin ):
    model = Member
    template_name = 'family/member_form.html'
    fields = '__all__'
    login_url = '/login/'




class MemberUpdate(UpdateView ,LoginRequiredMixin,AuthorAccessMixin ):
    model = Member
    template_name = 'family/member_form.html'
    fields = ('family','phone','t_saham' ,'status')
    success_url = reverse_lazy('family:person_list')

class MemberDelete(DeleteView ,LoginRequiredMixin ,AuthorAccessMixin):
    model = Member
    template_name = 'family/DeleteMember_form.html'
    success_url = reverse_lazy('family:person_list')


# dashboard view  
class DashbordView(generic.ListView ,LoginRequiredMixin ):
    model = Sandogh
    context_object_name = 'fund'
    template_name = 'family/dashbord.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Sandogh.objects.all()
        else:
            return Sandogh.objects.filter(sandogh_id = self.request.user)

# member list view
class ListMemberView(generic.ListView , LoginRequiredMixin):
    model = Member
    context_object_name = "member_list"
    template_name = "family/memberlist.html"

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Member.objects.all()
        else:
            return Member.objects.filter(author=self.request.user).order_by('membership')


# loan create view update view delete view
class LoanCreate(CreateView ,LoginRequiredMixin , FieldsMixin ):
    model = Loan
    template_name = 'family/loan_form.html'
    fields = '__all__'
    login_url = '/login/'

class ListLoanView(generic.ListView , LoginRequiredMixin):
    model = Loan
    context_object_name = "loan_list"
    template_name = "family/loanlist.html"

    def get_queryset(self):
        if self.request.user.is_superuser :
            return Loan.objects.all()
        else:
            return Loan.objects.filter(author=self.request.user)

class LoanUpdate(UpdateView , LoginRequiredMixin,AuthorAccessMixin ):
    model = Loan
    template_name = 'family/loan_form.html'
    fields = ("m_vam","m_ghest","t_gest","choice")
    success_url = reverse_lazy('family:vam_list')


class LoanDelete(DeleteView ,LoginRequiredMixin ,AuthorAccessMixin):
    model = Loan
    template_name = 'family/DeleteLoan_form.html'
    success_url = reverse_lazy('family:vam_list')
             
@login_required
def lottory(request ,pk ):
    
    winner_form = LottoryForm()
    if request.method == 'POST':
       winner_form = LottoryForm( request.POST)
       query = Member.objects.state()
       loan = Loan.objects.get(id = pk)
       ids = list(query.values_list('name','family'))
       winner = random.choice(ids)
       winner1 = Lottory.objects.create(name=winner[0],family=winner[1] , loan = loan  ) 
       winner_form = winner1
       winner_form.save()
       return redirect("family:winner_list")    
    context ={
        "winnerform" :winner_form
    } 
              
    return render(request ,'family/lottory.html' ,context)


class WinnerListview(generic.ListView):
    model = Lottory
    context_object_name = 'winner_list'
    template_name = 'family/winnerlist.html'

    def get_queryset(self):
        return Lottory.objects.all()

class WinnerDeleteView(DeleteView ,LoginRequiredMixin ,AuthorAccessMixin):
    model = Lottory
    template_name = 'family/DeleteWinner_form.html'
    success_url = reverse_lazy('family:vam_list')

                       