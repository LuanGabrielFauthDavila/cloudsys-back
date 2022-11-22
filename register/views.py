from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.datastructures import MultiValueDictKeyError

from default.views import verifyLogin
 
from . import forms
from . import models
import json


@csrf_exempt
def addProduct(request):
    if request.method == "POST":
        body = json.loads(request.body)
        body["company"] = int(body["company"])
        body["company_worker"] = int(body["company_worker"])
        
        print(body)
        if body["type"] == 1:
            form = forms.AddProductForm(body)
            print(form.is_valid())
            if form.is_valid():
                form.save()
                return HttpResponse(status=200, headers={'content-type': 'application/json'})
            return HttpResponse("Access violation", status=401, headers={'content-type': 'application/json'})
        elif body["type"] == 2:
            form = forms.AddProductSaleForm(body)
            if form.is_valid():
                last_id = form.save().id
                return HttpResponse(last_id, status=200, headers={'content-type': 'application/json'})
            return HttpResponse("Access violation", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Access violation", status=402, headers={'content-type': 'application/json'})

@csrf_exempt
def editProduct(request):
    if request.method == "POST":
        body = json.loads(request.body)
        if body["type"] == 2:
            prod = models.Product.objects.filter(company= body["company"], id=body["id"])
            if prod[0].name != body["name"]:
                prod.update(name=body["name"])
            if prod[0].price != body["price"]:
                prod.update(price=body["price"])    
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Access violation", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Access violation", status=402, headers={'content-type': 'application/json'})

@csrf_exempt
def deleteProduct(request):
    if request.method == "POST":
        body = json.loads(request.body)
        if int(body["type"]) == 1:
            model = models.Product.objects.filter(company= body["company"], id=body["id"])
            if len(model) > 0:
                return HttpResponse(status=201, headers={'content-type': 'application/json'})
            else:
                model.delete()
                return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Access violation", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Access violation", status=402, headers={'content-type': 'application/json'})

@csrf_exempt
def deleteProductSale(request):
    if request.method == "POST":
        body = json.loads(request.body)
        if int(body["type"]) == 2:
            modelitem = models.ProductItems.objects.filter(company= body["company"], product= body["product"])
            model = models.Product.objects.filter(company= body["company"], id= body["product"])
            for m in modelitem:
                m.delete()
            model.delete()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        elif int(body["type"]) == 1:
            models.ProductItems.objects.filter(company= body["company"], product= body["product"], product_item= body["product_item"]).delete() 
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Access violation", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Access violation", status=402, headers={'content-type': 'application/json'})

def getProduct(request):
    if request.method == "GET":
        try:
            get = dict(request.GET)
        except MultiValueDictKeyError:
            get = []
            return HttpResponse("Invalid data!", status=401, headers={'content-type': 'application/json'})
        if verifyLogin(get['token']):
            model = models.Product.objects.filter(company=get['company'][0], type=get['type'][0])
            data = []
            for m in model:
                data.append({
                    'id': str(m.id),
                    'name': str(m.name),
                    'brand': str(m.brand),
                    'measure': str(m.measure),
                    'stock': str(m.stock),
                    'cost': str(round(m.cost,2)),
                    'price': str(m.price),
                    'type': str(m.type)
                })
            return HttpResponse(json.dumps(data), status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Access violation", status=402, headers={'content-type': 'application/json'})

def setProductCost(id, company):
    model = models.ProductItems.objects.filter(company=company, product=id)
    data = []
    cost = 0
    quantity = 0

    for m in model:
        cost += m.product_item.cost*m.quantity
        quantity += m.quantity

        data.append({
            'id': str(m.id),
            'cost': str(m.product_item.cost),
        })
    if quantity == 0:
        return 0
    else:    
        return cost/quantity


@csrf_exempt
def addProductItems(request):
    if request.method == "POST":
        body = json.loads(request.body)
        print(request.body)
        cost = 0
        for i in body["items"]:
            form = forms.AddProductItemsForm({
                "company": body["company"],
                "company_worker": body["company_worker"],
                "product": body["product_sale"],
                "product_item": i["id"],
                "quantity": i["quantity"],
            })
            if form.is_valid():
                form.save()
            cost += setProductCost(body["product_sale"], body["company"])
        models.Product.objects.filter(company=body["company"], id=body["product_sale"]).update(cost=cost)
        return HttpResponse(status=200, headers={'content-type': 'application/json'})
    return HttpResponse("Access violation", status=402, headers={'content-type': 'application/json'})

@csrf_exempt
def addProductItem(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddProductItemsForm(body)
        if form.is_valid():
            models.Product.objects.filter(company=body["company"], id=body["product_sale"]).update()
        return HttpResponse(status=200, headers={'content-type': 'application/json'})
    return HttpResponse("Access violation", status=402, headers={'content-type': 'application/json'})

def getProductItems(request):
    if request.method == "GET":
        try:
            get = dict(request.GET)
        except MultiValueDictKeyError:
            get = []
            return HttpResponse("Invalid data!", status=401, headers={'content-type': 'application/json'})
        if verifyLogin(get['token'][0]):
            model = models.ProductItems.objects.filter(company=get['company'][0], product=get['product'][0])
            data = []
            for m in model:
                data.append({
                    'id': str(m.id),
                    'prod': str(m.product.id),
                    'prod_item': str(m.product_item.id),
                    'name': str(m.product_item.name),
                    'measure': str(m.product_item.measure),
                    'quantity': str(m.quantity),
                    'cost': str(round(m.product_item.cost,2)),
                    'price': str(m.product_item.price),
                })
            return HttpResponse(json.dumps(data), status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Access violation", status=402, headers={'content-type': 'application/json'})
    return HttpResponse("Access violation", status=403, headers={'content-type': 'application/json'})

@csrf_exempt
def addBrand(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddBrandForm(body)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Access violation", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Access violation", status=402, headers={'content-type': 'application/json'})

def getBrand(request):
    if request.method == "GET":
        try:
            get = dict(request.GET)
        except MultiValueDictKeyError:
            get = []
            return HttpResponse("Invalid data!", status=401, headers={'content-type': 'application/json'})
        if verifyLogin(get['token']) == 200:
            data = []
            for m in models.ProductBrand.objects.filter(company=get['company'][0]):
                data.append({
                    'brand_id': m.id,
                    'brand_name': m.brand,
                })
            return HttpResponse(json.dumps(data), status=200, headers={'content-type': 'application/json'})
        return HttpResponse(status=401, headers={'content-type': 'application/json'})

@csrf_exempt
def addMeasure(request):
    if request.method == "POST":
        body = json.loads(request.body)
        form = forms.AddMeasureForm(body)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Access violation", status=401, headers={'content-type': 'application/json'})
    return HttpResponse("Access violation", status=402, headers={'content-type': 'application/json'})

def getMeasure(request):
    if request.method == "GET":
        try:
            get = dict(request.GET)
        except MultiValueDictKeyError:
            get = []
            return HttpResponse("Invalid data!", status=401, headers={'content-type': 'application/json'})
        if verifyLogin(get['token']) == 200:
            data = []
            for m in models.ProductMeasure.objects.filter(company=get['company'][0]):
                data.append({
                    'measure_id': m.id,
                    'measure_name': m.measure,
                })
            return HttpResponse(json.dumps(data), status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Access violation", status=401, headers={'content-type': 'application/json'})

@csrf_exempt
def addProductStock(request):
    if request.method == "POST":
        body = json.loads(request.body)
        model = models.Product.objects.filter(company=body["company"],id=body["product"])
        for m in model:
            mod = m.cost*m.stock
            front = float(body["quantity"])*float(body["cost"])
            base = m.stock+float(body["quantity"])
            if m.stock == 0 or base == 0:
                model.update(stock=base,cost=body["cost"])
            else:
                model.update(stock=round(base,2),cost=(mod+front)/base) 
        return HttpResponse(status=200, headers={'content-type': 'application/json'})
    return HttpResponse("Access violation", status=402, headers={'content-type': 'application/json'})
    
@csrf_exempt
def addPartner(request):
    if request.method == "POST":
        body = json.loads(request.body)
        if verifyLogin(body["token"]):
            form = forms.AddPartnerForm(body)
            print(body)
            if form.is_valid():
                form.save()
                return HttpResponse(status=200, headers={'content-type': 'application/json'})
            return HttpResponse("Access violation", status=401, headers={'content-type': 'application/json'})
        return HttpResponse("Access violation", status=402, headers={'content-type': 'application/json'})
    return HttpResponse("Access violation", status=403, headers={'content-type': 'application/json'})

def getPartner(request):
    if request.method == "GET":
        try:
            get = dict(request.GET)
        except MultiValueDictKeyError:
            get = []
            return HttpResponse("Invalid data!", status=401, headers={'content-type': 'application/json'})

        if verifyLogin(get['token']) == 200:
            data = []
            for m in models.Partner.objects.filter(company=get['company'][0]):
                try:
                    city = m.city.id
                except:
                    city = ''
                data.append({
                    'id': str(m.id),
                    'person_f_j': m.person_f_j,
                    'type_client': m.type_client,
                    'type_provider': m.type_provider,
                    'type_conveyor': m.type_conveyor,
                    'name': m.name,
                    'fantasy': m.fantasy,
                    'cpf_cnpj': m.cpf if m.cpf != None else m.cnpj,
                    'rg_ie': m.rg if m.rg != None else m.ie,
                    'phone_number': m.phone_number,
                    'email': m.email,
                    'cep': m.cep,
                    'street': m.street,
                    'district': m.district,
                    'city': city,
                    'num': m.num,
                })
            return HttpResponse(json.dumps(data, indent=3), status=200, headers={'content-type': 'application/json'})
        return HttpResponse("Access violation", status=401, headers={'content-type': 'application/json'})

@csrf_exempt
def editPartner(request):
    if request.method == "POST":
        body = json.loads(request.body)
        if verifyLogin(body["token"]):
            form = forms.AddPartnerForm(body)
            print(body)
            if form.is_valid():
                form.save()
                return HttpResponse(status=200, headers={'content-type': 'application/json'})
            return HttpResponse("Access violation", status=401, headers={'content-type': 'application/json'})
        return HttpResponse("Access violation", status=402, headers={'content-type': 'application/json'})
    return HttpResponse("Access violation", status=403, headers={'content-type': 'application/json'})

@csrf_exempt
def deletePartner(request):
    if request.method == "POST":
        body = json.loads(request.body)
        if verifyLogin(body["token"]):
            form = forms.AddPartnerForm(body)
            print(body)
            if form.is_valid():
                form.save()
                return HttpResponse(status=200, headers={'content-type': 'application/json'})
            return HttpResponse("Access violation", status=401, headers={'content-type': 'application/json'})
        return HttpResponse("Access violation", status=402, headers={'content-type': 'application/json'})
    return HttpResponse("Access violation", status=403, headers={'content-type': 'application/json'})



