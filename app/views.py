from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def form(request):                 #post method is active when request came with data
    if request.method=='POST':     #if the request call the function with data then it will return that HttpResponse
        name=request.POST['un']
        password=request.POST['pw']
        print(f'The Login form  holder name is {name} and his possword is {password} ')
        return HttpResponse(f"<h1>{name}'s Form is submitted</h1>")
    return render(request,'form.html')  #if the request call the function date then it will this Display Form