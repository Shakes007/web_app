from django.shortcuts import render
from .models import Band

# Create your views here.


# Function to render a page with names of different bands.
def band_list(request):
    '''Home page'''
    bands = Band.objects.all()
    return render(request, 'music/band_list.html', {'bands': bands})


def tour_dates(request):
    '''Tour dates page to show vacancy of tickets'''
    return render(request, 'music/tour_dates.html')


def contact(request):
    '''Conact page to show form for fan mail.'''
    return render(request, 'music/contact.html')
