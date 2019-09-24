from django.utils import timezone

def format_duration(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    formated_duration = "{0} ч. {1} мин.".format(hours, minutes)
    return formated_duration


def get_duration(visit):
    present_time = timezone.now()
    if not visit.leaved_at:
      duration = duration = present_time - visit.entered_at
    else: 
      duration = visit.leaved_at - visit.entered_at
    return duration.seconds