=====================
django_localflavor_gr
=====================

Country-specific Django helpers for Greece.

What's in the greek localflavor?
=================================

* forms.GRPostalCodeField: Greek Postal code field. The valid format is
  5 digits and not starting with 0 or 9.
  
* forms.GRTaxNumberCodeField: Greek Tax Number code field. The valid format is
  9 digits that pass a specific algorithm. You can add the allow_test_value kwarg
  to the field in order to allow the default test value of 000000000.
  
* GRPhoneNumberField: Greek 10-digit phone number (could start with +30)

* GRMobilePhoneNumberField: Same as GRPhoneNumberField but has to start with 69.
  
See the source code for full details.

Testing
=======

In order to be able to test, a test_settings.py file was added in the root of the
project tree and an empty django_localflavor_gr/models.py in order to include
django_localflavor_gr as a django application.

This is a small modification of myusuf3 's solution on https://github.com/myusuf3/django-localflavor-us 

To test, run 


    git clone https://github.com/spapas/django-localflavor-gr
    cd django-localflavor-gr
    django-admin.py test --settings=test_settings --pythonpath=.
    
    

About localflavors
==================

Django's "localflavor" packages offer additional functionality for particular
countries or cultures.

For example, these might include form fields for your country's postal codes,
phone number formats or government ID numbers.

This code used to live in Django proper -- in django.contrib.localflavor -- but
was separated into standalone packages in Django 1.5 to keep the framework's
core clean.

For a full list of available localflavors, see https://github.com/django/
