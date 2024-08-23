from django.http import HttpResponse
from django.shortcuts import render, redirect
from meetups.models import Meet, Participant
from .forms import RegistrationForm

# Create your views here.
def list(request):
    meetups= Meet.objects.all()
    
    context={ 'meetups':meetups}
    return render(request, 'meetups/list.html', context)


def create_student(request):
    
    stu = Meet(name="Maryamawit", age=7, school="")
    stu.save()
    
    return HttpResponse(f'Student {stu.name} created successfully.')


def index(request):

    meetingup =[
        {'title': 'A First Meetup'},
        {'title': 'A Second Meetup'}
    ]

    context = {'met': meetingup, 'show_meetups': True}
    return render(request, 'index.html', context)


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meet.objects.get(slug = meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registartion_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registartion_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

        context ={'meetup_found': True,
                  'meetup': selected_meetup,
                  'form': registration_form }   
        return render(request, 'meetups/details.html', context)        
    except Exception as exc:
        return render(request, 'meetups/registration-success.html', {'meetup_found': True})


def confirm_registration(request, meetup_slug):
    meetup= Meet.objects.get(slug =meetup_slug)
    return render(request, 'meetups/registration-success.html',{
        'organizer_email':meetup.organizer_email})


