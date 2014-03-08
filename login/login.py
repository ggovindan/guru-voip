from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

def signin(request):
    username = password = ""
    if request.POST:
      username = request.POST.get("username")
      password = request.POST.get("password")
      user = authenticate(username=username, password=password)

      if user is not None:
          if user.is_active:
              login(request, user)
              return HttpResponseRedirect('/guru-voip/mainpage/?username='+username)
          else:
              return render_to_response('auth.html', {"state": state, "username": username}, context_instance=RequestContext(request)) 
      else:
          return HttpResponseRedirect('/guru-voip/')
        # Return an 'invalid login' error message.

    return render_to_response('login.html', {"username": username}, context_instance=RequestContext(request)) 

@login_required
def mainpage(request):
    user_data = User.objects.get(username=unicode(request.user))
    if user_data is not None:
        return render_to_response('mainpage.html', {"username": user_data.username}, context_instance=RequestContext(request))    

