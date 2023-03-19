from django.shortcuts import render
from Insertemp.models import dbins
from django.contrib import messages

def insert(request):
    if request.method=='POST':
        print("ok")
       # image=request.POST.get['image']
        #name = request.POST['name']
        #email = request.POST['email']
        #phone = request.POST['phone']
        #address = request.POST['address']
        #experience=request.POST.get['experience']
        #education=request.POST.get['education']
        if request.POST.get('image') and request.POST.get('name') and request.POST.get('email') and request.POST.get('phone') and request.POST.get('address') and request.POST.get('education') and request.POST.get('experience'):
            saverecord=dbins()
            saverecord.image=request.POST.get('image')
            saverecord.name=request.POST.get('name')
            saverecord.email=request.POST.get('email')
            saverecord.phone=request.POST.get('phone')
            saverecord.address=request.POST.get('address')
            saverecord.experience=request.POST.get('experience')
            saverecord.education=request.POST.get('education')
            saverecord.save()
            messages.success(request,'recored saved successfully')
            return render(request, 'cv.html', {
            'image': saverecord.image,
            'name': saverecord.name,
            'email': saverecord.email,
            'phone': saverecord.phone,
            'address': saverecord.address,
            'experience': saverecord.experience,
            'education': saverecord.education,
            })
    else:
            return render(request,'reject.html')