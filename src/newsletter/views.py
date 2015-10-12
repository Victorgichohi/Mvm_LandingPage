from django.shortcuts import render

# Create your views here.
def home(request):
    title= "hello meen"
    if request.user.is_authenticated():
        title = "My Title %s" %(request.user)


    context={
        "title":title,
        }
    return render(request,"home.html", context)
