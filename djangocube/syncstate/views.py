from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.template import loader, Context, RequestContext
from django.contrib.auth.decorators import login_required

from syncstate.models import Squares

def home(request):
    return render_to_response("home.html", context_instance=RequestContext(request))


def poll(request):
    """Returns the Squares object. In JSON form.
    """

    square = get_object_or_404(Squares, pk=1)

    return HttpResponse(square.render(), mimetype='text/plain' )

def rotate(request):
    if request.method == 'POST':
        square = get_object_or_404(Squares, pk=1)
        square.rotate()
        square.save()
        return HttpResponse(square.render(), mimetype='text/plain' )
    else:
        return HttpResponse("{'error':'Post required'}", mimetype='text/plain' )
        

