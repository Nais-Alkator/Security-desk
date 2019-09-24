from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from secondary_functions import format_duration, get_duration
from django.http import Http404


def is_visit_long(visit):
    duration = get_duration(visit)
    return duration > 3600


def passcard_info_view(request, passcode):
    try:
        first_passcard = Passcard.objects.get(passcode=passcode)
    except first_passcard.DoesNotExist:
        raise Http404("No Passcard matches the given query.")

    visits = Visit.objects.filter(passcard=first_passcard)

    this_passcard_visits = []

    for visit in visits:
        duration = get_duration(visit)
        this_passcard_visit = [
          {
            "entered_at": visit.entered_at,
            "duration": format_duration(duration),
            "is_strange": is_visit_long(visit)
          },
        ]
        this_passcard_visits.extend(this_passcard_visit)

    context = {
        "passcard": first_passcard,
        "this_passcard_visits": this_passcard_visits
        }
    return render(request, 'passcard_info.html', context)
