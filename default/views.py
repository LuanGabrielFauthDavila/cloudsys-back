from django.shortcuts import render, HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt

from . import forms
from . import models
import json
import requests as r


@csrf_exempt
def login(request):
    body = json.loads(request.body)
    email = body['email']
    password = body['password']
    User = models.User.objects.get(email=email)
    req = r.post('http://127.0.0.1:80/auth/jwt/create/', {
        'username': User.username,
        'password': password
    })
    data = {
        'login_token': req.json(),
        'user_id': User.id,
        'username': User.username,
        'email': User.email
    } 

    return HttpResponse(json.dumps(data), status=200, headers={'content-type': 'application/json'})

def verifyLogin(token):
    req = r.post('http://127.0.0.1:80/auth/jwt/verify/', {
        'token': token,
    })
    return req.status_code
@csrf_exempt
def register(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.NewRegisterForm(body)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=401, headers={'content-type': 'application/json'})
    
def getCompany(request):
    try:
        email = request.GET['email']
    except MultiValueDictKeyError:
        return HttpResponse("Cannot find your email!", status=401, headers={'content-type': 'application/json'})
    try:
        key = request.GET['key']
    except MultiValueDictKeyError:
        return HttpResponse("Cannot find your key!", status=401, headers={'content-type': 'application/json'})

    if key == '8168':
        user = models.User.objects.get(email=email)
        companyworker = models.CompanyWorker.objects.filter(person=user).order_by('company')
        comp = []
        for w in companyworker:
            comp.append({
                'company_id': str(w.company.id),
                'company': str(w.company.company),
                'slug': str(w.company.slug),
                'email': str(w.person.email),
                'first_name': str(w.person.first_name), 
                'last_login': str(w.person.last_login)
            })
        return HttpResponse(json.dumps(comp), status=200, headers={'content-type': 'application/json'})
    else:
        return HttpResponse("Cannot find your key!", status=401, headers={'content-type': 'application/json'})

@csrf_exempt
def addBugReport(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddBugReportForm(body)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Invalid form!", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Need be a POST", status=401, headers={'content-type': 'application/json'})