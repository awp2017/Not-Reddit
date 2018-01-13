# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from Readit.models import Post


class MyForm(forms.ModelForm):
	class Meta:
		# model = NumeModel
		# fields = ('field', 'field')
		pass

#form-urile Dianei


#form-urile Mădălinei

class PostEditForm(forms.ModelForm):
    class Meta:
    	model = Post
    	fields = ('title', 'text', 'link')


#form-urile lui Claudiu


#form-urile lui Dutzu 