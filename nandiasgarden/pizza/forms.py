from django import forms
from .models import Pizza

class PizzaForm(forms.Form):
    topping1 = forms.CharField(label='Topping 1', max_length=100)
    topping2 = forms.CharField(label='Topping 2', max_length=100)
    # toppings = forms.MultipleChoiceField(choices=[('pep','Pepperoni'),('cheese','Cheese'),('olives','Olives'),('onion','Onion')], widget=forms.CheckboxSelectMultiple)
    size = forms.ChoiceField(label='Size', choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Extra Large', 'Extra Large')])

# class PizzaForm(forms.ModelForm):
#     class Meta:
#         model = Pizza
#         fields = ['topping1', 'topping2', 'size']
#         labels = {'topping1':'Topping 1', 'topping2':'Topping 2'}
