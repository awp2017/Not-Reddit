# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from Readit.models import Post, UserProfile, Category

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from Readit.models import UserProfile, Comment

class MyForm(forms.ModelForm):
	class Meta:
		# model = NumeModel
		# fields = ('field', 'field')
		pass

#form-urile Dianei

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditUserProfile(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('description', 'image_url')


#form-urile Mădălinei

class PostEditForm(forms.ModelForm):
    class Meta:
    	model = Post
    	fields = ('title', 'text', 'link')

class CommentEditForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('text',)


#form-urile lui Claudiu

class PostAddForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'link', 'category')


#form-urile lui Dutzu 