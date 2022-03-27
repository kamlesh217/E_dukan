from products.models import *

def Details_context(item_id):
    context={
    "ram":RAM.objects.filter(product=item_id).first ,
    "rom":ROM.objects.filter(product=item_id).first,
    "ssd":SSD.objects.filter(product=item_id).first,
    "battery_desc":Battery_desc.objects.filter(product=item_id).first,
    "battery_power":Battery_power.objects.filter(product=item_id).first,
    "connectivity":Connectivity_technologies.objects.filter(product=item_id).first,
    "box":BOX.objects.filter(product=item_id).first,
    "manufacturer":Manufacturer.objects.filter(product=item_id).first,
    "origin":Country_of_origin.objects.filter(product=item_id).first,
    "weight":Item_weight.objects.filter(product=item_id).first,
    "display_desc":Display_desc.objects.filter(product=item_id).first,
    "display_size":Display_size.objects.filter(product=item_id).first,
    "camera_desc":Camera_desc.objects.filter(product=item_id).first,
    "camera_front":Camera_front.objects.filter(product=item_id).first,
    "camera_rear":Camera_rear.objects.filter(product=item_id).first,
    "os":OS.objects.filter(product=item_id).first,
    "special":Special_features.objects.filter(product=item_id).first,
    "review":Reviews.objects.filter(product=item_id).reverse()[:5],
    "review_count":Reviews.objects.filter(product=item_id).count
    }
    return context


