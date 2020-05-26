from django.shortcuts import render
from .models import Job


def setGlobal():
    globalInfo = {'name': 'David Wachtel',
                  'jumboText': ('In the trenches and in the board room - I have led a public company out of bankruptcy,'
                                ' growing it to record earnings; played an integral part raising venture capital, as well as in the buying,'
                                'selling and merging of numerous companies.'
                                'I have led large technology teams, built leading edge technology solutions and have built and run start ups'
                                'while repeatedly demonstrating effectiveness by blending strong technology skills, strategy and ideas and leadership.'
                                'Specialties: Leadership, Public Company ceo and cto, Strategy, Product and Market Conception'
                                )
                  }
    return(globalInfo)


def home(request):
    gi = setGlobal()

    jobList = Job.objects
    return render(request, 'home.html', {'navName': gi['name'],
                                         'jumboText': gi['jumboText'],
                                         'jobList': jobList,
                                         })
