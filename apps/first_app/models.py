from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
# Create your models here.
class UserManager(models.Manager):
    def registerVal(self, postData):
        results = {'status': True, 'errors': []}
        user = []

        if not postData['first_name'] or len(postData['first_name']) < 3:
            results['status'] = False
            results['errors'].append('First name needs to be longer than 2 characters.')

        if not postData['last_name'] or len(postData['last_name']) < 3:
            results['status'] = False
            results['errors'].append('Last name needs to be longer than 2 characters.')

        if not postData['email'] or len(postData['email']) < 5 or not re.match(r"[^@]+@[^@]+\.[^@]+", postData['email']):
            results['status'] = False
            results['errors'].append('Email is invalid')

        if not postData['password'] or len(postData['password']) < 5:
            results['status'] = False
            results['errors'].append('Password needs to be at least 5 characters long.')

        if results['status'] == True:
            user = User.objects.filter(email = postData['email'])

        if len(user) != 0:
            results['status'] = False
            results['errors'].append('User already exists. Please try another email.')

        print results['status']
        print results['errors']
        return results


    def loginVal(self, postData):
        results = {'status':True, 'errors': [], 'user': None}

        if len(postData['email']) < 3:
            results['status'] = False
            results['errors'].append('Something went wrong. Double check everything.')

        else:
            user = User.objects.filter(email = postData['email'])

            if len(user) <= 0:
                results['status'] = False
                results['errors'].append('Something went wrong. Double check everything.')

            elif len(postData['password']) < 5 or postData['password'] != user[0].password:
                results['status'] = False
                results['errors'].append('Something went wrong. Double chekc everything.')

            else:
                results['user'] = user[0]

        print results['status']
        print results['errors']
        return results

    def createUser(self, postData):
        p_hash = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
        user = User.objects. create(first_name = postData['first_name'], last_name = postData['last_name'], email = postData['email'], password = postData['password'])
        return user


class User(models.Model):
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
