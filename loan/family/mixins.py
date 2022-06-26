from django.http import Http404
from django.shortcuts import get_object_or_404
from .models import Member

class FieldsMixin():

    def dispatch(self, request,*args, **kwargs):
        if request.user.is_superuser :
            self.fields =[
                "sandogh","name","saham","m_saham","m_sandogh","shomare_hesab"
            ]
        elif request.user == request.user.is_staf:
            self.fields = [
                "sandogh", "name", "saham", "m_saham", "m_sandogh", "shomare_hesab"
            ]
        else:
            raise Http404("شما نمیتانید این صفحه را ببینید")

        return super().dispatch(request, *args, **kwargs)

class AuthorAccessMixin():
    def dispatch(self,request,pk,*args,**kwargs):
        members = get_object_or_404(Member, pk=pk)
        if request.user == request.user.is_staf or request.user.is_superuser:
            return super().dispatch(request,*args,**kwargs)
        else:
            raise Http404("شما دسترسی به این صفحه ندارید")


