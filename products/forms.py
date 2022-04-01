from django import forms
from .models import *

class SSD_form(forms.ModelForm):
    class Meta:
        model = SSD
        fields = ("ssd","product")
    
class RAM_form(forms.ModelForm):
    class Meta:
        model = RAM
        fields = ("ram",)

class ROM_form(forms.ModelForm):
    class Meta:
        model = ROM
        fields = ("rom",)

class Display_desc_form(forms.ModelForm):
    class Meta:
        model = Display_desc
        fields = ("desc","product")

class Display_size_form(forms.ModelForm):
    class Meta:
        model = Display_size
        fields = ("size",)

class Battery_power_form(forms.ModelForm):
    class Meta:
        model = Battery_power
        fields = ("power",)

class Battery_desc_form(forms.ModelForm):
    class Meta:
        model = Battery_desc
        fields = ("desc",)

class Camera_front_form(forms.ModelForm):
    class Meta:
        model = Camera_front
        fields = ("front",)

class Camera_rear_form(forms.ModelForm):
    class Meta:
        model = Camera_rear
        fields = ("rear",)

class Camera_desc_form(forms.ModelForm):
    class Meta:
        model = Camera_desc
        fields = ("desc",)

class OS_form(forms.ModelForm):
    class Meta:
        model = OS
        fields = ("os",)

class Connectivity_technologies_form(forms.ModelForm):
    class Meta:
        model = Connectivity_technologies
        fields = ("desc",)

class Special_features_form(forms.ModelForm):
    class Meta:
        model = Special_features
        fields = ("desc",)

class BOX_form(forms.ModelForm):
    class Meta:
        model = BOX
        fields = ("desc",)

class Manufacturer_form(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ("desc",)

class Country_of_origin_form(forms.ModelForm):
    class Meta:
        model = Country_of_origin
        fields = ("country",)

class Item_weight_form(forms.ModelForm):
    
    class Meta:
        model = Item_weight
        fields = ("weight",)


class Other_image_form(forms.ModelForm):
    
    class Meta:
        model = Other_image
        fields = ("image",)

