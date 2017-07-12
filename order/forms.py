from django import forms

from .models import Product, return_order, Order


class return_orderForm(forms.ModelForm):
    class Meta:
        model = return_order
        fields = ('orderid', 'ProductId', 'ReturnReason', 'ReturnOptions', 'ProductQuality')

    def __init__(self, user, *args, **kwargs):
        super(return_orderForm, self).__init__(*args, **kwargs)
        self.fields['orderid'].queryset = Order.objects.filter(oPurchaser=user)
        self.fields['ProductId'].queryset = Product.objects.filter(ProBuyer=user)

class product_orderForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['ProdId', 'OrderQuantity']

    def __init__(self, user, *args, **kwargs):
        super(product_orderForm, self).__init__(*args, **kwargs)
        self.fields['ProdId'].queryset = Product.objects.filter(ProBuyer=user)