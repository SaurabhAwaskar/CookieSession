# demo/views.py
from django.shortcuts import render
from django.http import HttpResponse

def set_cookie_session(request):
    response = HttpResponse("Cookie and Session Set!")
    
    # Set a cookie
    response.set_cookie('example_cookie', 'cookie_value')

    # Set a session variable
    request.session['example_session'] = 'session_value'

    return response

def show_info(request):
    # Retrieve cookie and session information
    cookie_value = request.COOKIES.get('example_cookie', 'Not set')
    session_value = request.session.get('example_session', 'Not set')

    # Display information in a template
    return render(request, 'show_info.html', {'cookie_value': cookie_value, 'session_value': session_value})

