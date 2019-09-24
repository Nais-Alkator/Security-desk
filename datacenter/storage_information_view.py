from datacenter.models import Visit
from django.shortcuts import render
from secondary_functions import format_duration, get_duration


def storage_information_view(request):
    not_leaved = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []
    for item in not_leaved:
        duration = get_duration(item)
        duration_text = format_duration(duration)
        non_closed_visit = [
            {
                "who_entered": item.passcard,
                "entered_at": item.entered_at,
                "duration": duration_text,
            }
        ]
        non_closed_visits.extend(non_closed_visit)

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
