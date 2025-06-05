from django.db import models

# Create your models here.

class Education(models.Model):
    school = models.CharField("Skole", max_length=200)
    degree = models.CharField("Grad / Utdanning", max_length=200)
    field_of_study = models.CharField("Studieretning", max_length=200)
    start_date = models.DateField("Startdato")
    end_date = models.DateField("Sluttdato", null=True, blank=True)
    description = models.TextField("Beskrivelse", blank=True)

    def __str__(self):
        return f"{self.degree} ved {self.school}"

class Experience(models.Model):
    job_title = models.CharField("Stilling", max_length=200)
    company = models.CharField("Arbeidsgiver", max_length=200)
    start_date = models.DateField("Startdato")
    end_date = models.DateField("Sluttdato", null=True, blank=True)
    description = models.TextField("Beskrivelse", blank=True)

    def __str__(self):
        return f"{self.job_title} hos {self.company}"

class Project(models.Model):
    title = models.CharField("Prosjekttittel", max_length=200)
    description = models.TextField("Beskrivelse")
    link = models.URLField("Lenke", blank=True)
    date = models.DateField("Dato")

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField("Ferdighet", max_length=100)
    level = models.CharField("Nivå", max_length=100, blank=True)

    def __str__(self):
        return self.name

class About(models.Model):
    content = models.TextField("Om meg-tekst")

    def __str__(self):
        return "Om meg"

class ContactMessage(models.Model):
    name = models.CharField("Navn", max_length=100)
    email = models.EmailField("E-post")
    subject = models.CharField("Emne", max_length=200)
    message = models.TextField("Melding")
    created_at = models.DateTimeField("Sendt", auto_now_add=True)

    def __str__(self):
        return f"Melding fra {self.name}"
