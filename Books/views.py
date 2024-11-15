from django.shortcuts import render,redirect
from Books.models import Book
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request,"home.html")

@login_required
def viewbooks(request):

    # k=modelname.objects.all()

    k=Book.objects.all() # reads all the records from the book table
    context={'book':k}  # sends data from view function to html page
    return render(request,"viewbooks.html",context)

@login_required
def addbooks(request):
    if(request.method=="POST"):
        t=request.POST['t']
        a=request.POST['a']
        pr=request.POST['pr']
        pa=request.POST['pa']
        l=request.POST['l']
        c=request.FILES['c']
        p=request.FILES['p']

        b=Book.objects.create(title=t,author=a,price=pr,pages=pa,languages=l,cover=c,pdf=p)
        b.save()
        # return redirect('addbooks')
        return viewbooks(request)
    return render(request,"addbooks.html")

@login_required
def viewbookdetails(request,p):
    print(p)
    k=Book.objects.get(id=p)  #reads aparticular
    # Need to read details of a particular book
    context={'book':k}
    return render(request,'viewbookdetails.html',context)

@login_required
def delete(request,p):
    k=Book.objects.get(id=p)
    k.delete()
    return redirect('Books:viewbooks')

@login_required
def edit(request,p):
    k=Book.objects.get(id=p)
    if(request.method=="POST"):
        k.title=request.POST['t']
        k.author=request.POST['a']
        k.price=request.POST['pr']
        k.pages=request.POST['pa']
        k.languages=request.POST['l']
        
        if(request.FILES.get('c')==None):
            k.save()
        else:
            k.cover=request.FILES.get('c')

        if(request.FILES.get('p')==None):
            k.save()
        else:
            k.cover=request.FILES.get('p')
        k.save()
        return redirect('Books:viewbooks')
    context={'book':k}
    return render(request,'edit.html',context)
