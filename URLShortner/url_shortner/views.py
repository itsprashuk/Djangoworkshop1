from django.shortcuts import render,redirect
from django.http import HttpResponse

from.models import LongtoShort



# Create your views here.
def hello_world(request):
    return HttpResponse("hey..........")

def task(request):
    context={
        "year":"2022",
        "firstname":"prashuk",
        "lastname":"jain"

        }

    return render(request,'task.html',context)
    
def  index(request):
    context={
        "submitted":False,
        "error":False

    }
    if(request.method)=="POST":
        #  print(request.POST)
        data=request.POST
        longurl=data['longurl']
        custom_name=data['custom_name']
        
        try:

            context['longurl']=longurl
            context["custom_name"]=request.build_absolute_uri() + custom_name
            
            obj=LongtoShort(long_url=longurl,custom_url=custom_name)
            obj.save()
            context["submitted"]=True
            context["date"]=obj.created_date
            context["clicks"]=obj.visit_count
        


        except:
            context["error"]=True  
       
       
        print(longurl,custom_name)
    else:
        print("not valid data")
    return render(request,'index.html',context) 


def redirect_url(request,customname):
    #  return HttpResponse(customname)
    row=LongtoShort.objects.filter(custom_url=customname)
    print(row)
    if len(row)==0:
        return HttpResponse("<h1 style=text-align:center>404 error!!!!</h1>")
    obj=row[0]
    long_url=obj.long_url
    obj.visit_count+=1
    obj.save()
    return redirect(long_url)
        

def analytics(request):
    rows=LongtoShort.objects.all()
    context={
        "rows":rows
    } 
    return render(request,"analytics.html",context) 



       

       


       
       
   

       



