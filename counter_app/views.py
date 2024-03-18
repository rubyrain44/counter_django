from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
def index(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 0
    return render(request, "index.html")

def destroy(request):
    del request.session['counter']	# clears a specific key
    return redirect('/')