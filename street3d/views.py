from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

# Create your views here.
def mapWithLocation(request,latLeft,lonLeft,latRight,lonRight,headingLeft,pitchLeft,zoomLeft,headingRight,pitchRight,zoomRight):
    return render(request,'3dview.html',{
                  'latLeft':latLeft,
                  'lonLeft':lonLeft,
                  'latRight':latRight,
                  'lonRight':lonRight,
                  'headingLeft':headingLeft,
                  'pitchLeft':pitchLeft,
                  'zoomLeft':zoomLeft,
                  'headingRight':headingRight,
                  'pitchRight':pitchRight,
                  'zoomRight':zoomRight});
def render_cross(request,latLeft,lonLeft,latRight,lonRight,headingLeft,pitchLeft,zoomLeft,headingRight,pitchRight,zoomRight):
    return render(request,'render.html',{
                  'latLeft':latLeft,
                  'lonLeft':lonLeft,
                  'latRight':latRight,
                  'lonRight':lonRight,
                  'headingLeft':headingLeft,
                  'pitchLeft':pitchLeft,
                  'zoomLeft':zoomLeft,
                  'headingRight':headingRight,
                  'pitchRight':pitchRight,
                  'zoomRight':zoomRight});
def map(request):
    return render(request,'3dview.html',{
                  'latLeft':46.407884,
                  'lonLeft':8.415076999999997,
                  'latRight':46.407773,
                  'lonRight':8.415253000000007,
                  'headingLeft':-131.2903721357681,
                  'pitchLeft':28.59928632833584,
                  'zoomLeft':1,
                  'headingRight':-131.2903721357681,
                  'pitchRight':28.59928632833584,
                  'zoomRight':1});


def db(request,latLeft,lonLeft,latRight,lonRight,headingLeft,pitchLeft,zoomLeft,headingRight,pitchRight,zoomRight):
    return render(request, 'db.html', {'greetings': "test"})

