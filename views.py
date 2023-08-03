# views.py
from django.shortcuts import render


def trainee(request):
    if request.method == 'POST':
        #trainee_id = request.POST['trainee_id']
        name = request.POST['name']
        age = request.POST['age']
        contact_number = request.POST['contact_number']
        email = request.POST['email']
        date_of_birth = request.POST['date_of_birth']
        print(name, age, contact_number, email,date_of_birth)
        trainee = trainee(name =name, contact_number=contact_number,email=email, date_of_birth = date_of_birth)
        trainee.save()
    return render(request, 'trainee/trainee.html')
