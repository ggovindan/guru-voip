# Create your views here.
from wiki.models import wikipage
from wiki.models import ClientAddress
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

#for admin view page
from django.core import serializers

from django.template import RequestContext
#import markdown

def viewpage(request, page_name):
	try:
		page = wikipage.objects.get(pk=page_name)
	except wikipage.DoesNotExist:
		return render_to_response("create.html", {"page_name": page_name}, context_instance=RequestContext(request))
	content = page.content
	return render_to_response("view.html", {"page_name": page_name, "content": content}, context_instance=RequestContext(request))

def editpage(request, page_name):
	try:
		page = wikipage.objects.get(pk=page_name)
		content = page.content
	except wikipage.DoesNotExist:
		content=""
	return render(request, "edit.html", {"page_name": page_name, "content": content}, context_instance=RequestContext(request))
def savepage(request, page_name):
	content = request.POST['content']
	try:
		page = wikipage.objects.get(pk=page_name)
		page.content = content
	except wikipage.DoesNotExist:
		#page = wikipage(pagename=page_name, content=markdown.markdown(content))
		page = wikipage(pagename=page_name, content=content)
	page.save()
	return HttpResponseRedirect("/mywiki/"+ page_name+ "/")

def mainpage(request, userid):
	#allcontent=wikipage.objects.distinct()
        try:
              ip = get_client_ip(request)
              client = ClientAddress.objects.get(pk=userid)
              client.currentAddress = ip
        except ClientAddress.DoesNotExist:
              client = ClientAddress(userid=userid, currentAddress=ip)
        client.save()
        return HttpResponse("I have your Location!")

def adminpage(request):
        try:
             client = ClientAddress.objects.distinct()
             client_as_json = serializers.serialize('json', client)
             return HttpResponse(client_as_json)
        except ClientAddress.DoesNotExist:
             return HttpResponse("No User Data")
        

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
	
	
