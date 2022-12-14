from django.db import models
from django.contrib.auth.models import User

class NewRegister(models.Model):
    email = models.CharField(max_length=80, blank=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    phone_number = models.CharField(max_length=30, blank=False)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name, verbose_name_plural = "Novo Registro", "Novos Registros"
        ordering = ("created",)

class Company(models.Model):
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    slug = models.CharField(max_length=250, blank=False)
    company = models.CharField(max_length=30, blank=False)
    cnpj = models.CharField(max_length=19, blank=False)
    pix_key = models.CharField(max_length=19, blank=True, null=True, default="")
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company

    class Meta:
        verbose_name, verbose_name_plural = "Company", "Companys"
        ordering = ("company",)

class CompanyPosition(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    position = models.CharField(max_length=25, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.position
    
    class Meta:
        verbose_name, verbose_name_plural = "Company Position", "Company Positions"
        ordering = ("position",)

class CompanyWorker(models.Model):
    person = models.ForeignKey(User, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    position = models.ForeignKey(CompanyPosition, on_delete=models.PROTECT)
    cpf = models.CharField(max_length=14, blank=False)
    rg = models.CharField(max_length=14, blank=False)
    phone_number = models.CharField(max_length=14, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.person.username
    
    class Meta:
        verbose_name, verbose_name_plural = "Company Worker", "Company Workers"
        ordering = ("person",)


class BugReport(models.Model):
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    company_worker = models.ForeignKey(CompanyWorker, on_delete=models.PROTECT)
    bug = models.TextField(blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name, verbose_name_plural = "Bug Report", "Bug Reports"
        ordering = ("created",)

class Country(models.Model):
    cod = models.CharField(max_length=15, blank=False)
    name = models.CharField(max_length=30, blank=False)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name, verbose_name_plural = "Country", "Countries"
        ordering = ("created",)


class State(models.Model):
    cod = models.CharField(max_length=15, blank=False)
    name = models.CharField(max_length=30, blank=False)
    country = models.ForeignKey(Country, blank=False, on_delete=models.PROTECT)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name, verbose_name_plural = "State", "States"
        ordering = ("created",)


class City(models.Model):
    cod = models.CharField(max_length=15, blank=False)
    name = models.CharField(max_length=30, blank=False)
    cep = models.CharField(max_length=10, blank=False)
    state = models.ForeignKey(State, blank=False, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, blank=False, on_delete=models.PROTECT)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name, verbose_name_plural = "City", "Cities"
        ordering = ("created",)