from django.shortcuts import render

from .forms import SignUpForm
# Create your views here.
def home(request):
    title= "hello meen"
    # if request.user.is_authenticated():
    # title = "My Title %s" %(request.user)


    form = SignUpForm()
    context={
        "title":title,

        "form" : form
        }
    return render(request,"home.html", context)
