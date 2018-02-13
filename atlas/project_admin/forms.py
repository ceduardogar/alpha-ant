from django import forms

from .models import *

class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ['id', 'name', 'client', 'vendor', 'administrator']
		widgets = {
			'id' : forms.TextInput(attrs={'class':'form-control',}),
			'name' : forms.TextInput(attrs={'class':'form-control',}),
			'client' : forms.Select(attrs={'class':'form-control',}),
			'vendor' : forms.Select(attrs={'class':'form-control',}),
			'administrator' : forms.Select(attrs={'class':'form-control',}),
		}

class ClientForm(forms.ModelForm):
	class Meta:
		model = Client
		fields = ['name', 'address']
		widgets = {
			'name' : forms.TextInput(attrs={'class':'form-control',}),
			'address' : forms.Textarea(attrs={'class':'form-control',}),
		}

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = ['part_number', 'brand', 'description']
		widgets = {
			'part_number' : forms.TextInput(attrs={'class':'form-control',}),
			'brand' : forms.TextInput(attrs={'class':'form-control',}),
			'description' : forms.Textarea(attrs={'class':'form-control',}),
		}

class SupplierForm(forms.ModelForm):
	class Meta:
		model = Supplier
		fields = ['name', 'address', 'phone', 'email', 'contact', 'items']
		widgets = {
			'name' : forms.TextInput(attrs={'class':'form-control',}),
			'address' : forms.TextInput(attrs={'class':'form-control',}),
			'phone' : forms.TextInput(attrs={'class':'form-control',}),
			#'email' : forms.TextInput(attrs={'class':'form-control',}),
			'contact' : forms.TextInput(attrs={'class':'form-control',}),
			#'items' : forms.TextInput(attrs={'class':'form-control',}),
		}

class CostForm(forms.ModelForm):
	class Meta:
		model = Cost
		fields = ['price', 'unit']
		widgets = {
			#'item' : forms.TextInput(attrs={'class':'form-control',}),
			#'supplier' : forms.TextInput(attrs={'class':'form-control',}),
			'price' : forms.TextInput(attrs={'class':'form-control',}),
			'unit' : forms.TextInput(attrs={'class':'form-control',}),
		}

class RequisitionForm(forms.ModelForm):
	class Meta:
		model = Requisition
		fields = ['supplier', 'coin', 'supplier_is_unique', 'requested_items']
		widgets = {
			'supplier' : forms.TextInput(attrs={'class':'form-control',}),
			'coin' : forms.TextInput(attrs={'class':'form-control',}),
			#'supplier_is_unique' : forms.TextInput(attrs={'class':'form-control',}),
			#'requested_items': forms.TextInput(attrs={'class':'form-control',}),
		}

class RequestItemForm(forms.ModelForm):
	class Meta:
		model = RequestItem
		fields = ['item', 'quantity', 'date_required']
		widgets = {
			#'item' : forms.TextInput(attrs={'class':'form-control',}),
			'quantity' : forms.TextInput(attrs={'class':'form-control',}),
			'date_required' : forms.TextInput(attrs={'class':'form-control',}),
		}
