56om django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.template import  RequestContext
from loginpage.forms   import RegistrationForm , Loginform
from loginpage.models import Loginpage
from django.contrib.auth import authenticate , login , logout



def UserRegistration(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == 'POST ':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user( username=form.cleaned_data['username'], email= form.cleaned_data['email'] , password= form.cleaned_data['password'])
            user.save()
            loginpage = Loginpage(user=user,name =form.cleaned_data['name'],Birthday =form.cleaned_data['Birthday'])
            loginpage.save()
            return HttpResponseRedirect('/profile/')
        else:
            return render_to_response('register.html', {'form ' : form} , context_insance=RequestContext(request))
    else:
        form = RegistrationForm()
        context = ('form':form)
        return render_to_response('register.html',context , context_instance =RequestContext(request))










def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method == ' POST ':
        form =Loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            loginpage = authenticate( username=username , password=password)
            if loginpage is not None :
                login(request, loginpage)
                return HttpResponseRedirect('/profile/')
            else:
                return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
        else:
            return render_to_response('register.html', {'form': form} , context_instance=RequestContext(request))

    else:
        form = Loginform()
        context={'from' : form}
        return render_to_response('login.html' ,context ,context_instance =RequestContext(request))


def LogoutRequest(request) :
    logout(request)
    return HttpResponseRedirect('/')

