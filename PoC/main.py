"""
Author:RipRock
Date of last edit: 1/4/19
Purpose: This is a rough out test of a shipping program simpleship
Its meant as a proof of concept for when I go to learn backen web dev to make it as a web app
"""
from dataclasses import dataclass
"""Random is here for testing purposes"""
import random
shipping_items = []
@dataclass
class Delivery:# This might be kept becuase it will help making the way to fill into the database easier
    product: str
    quanity: int
    po_num: str
    tracking: str
    sig: bool
    tickprojnum: str
    location: str

def main():
    prefill()
    print(shipping_items)
    print(len(shipping_items))
def information_gather(): # this will be rewritten into a HTML forum
    """This is the true information gathering. This is more for the input"""
    num_of_items = int(input("How many items to input into the list?:"))
    while num_of_items != 0:
        print("Item #" + str(num_of_items) +" "+ "Information")
        product = input("What product is this:")
        quanity = int(input("How many?: "))
        po_num = input("What is the PO Number:")
        tracking = input("What is the Tracking Number:")
        sig = bool(input("Is the object Delivered?:"))
        tick_proj = input("What ticket or project is this for?:")
        location = input("WHere is the product Located:")
        package = Delivery(tag, product, quanity, po_num, tracking, sig, tick_proj, location)
        shipping_items.append(package)
        num_of_items -= 1
    print(shipping_items)
def check_to_recieve(): # Same concept as this but instead this will be pulling from mysql
    """This takes either the Tracking number or the client tag to check to see what the delivery status of the obkect is."""
    while True:
       refrence = input("What are we checking?(Possible Values are SN or Client tag) or are we adding items:")
       if refrence == "SN":
           sn = input("What is the shipping/tracking num?:")
           for i in shipping_items:
               if i.tracking_num == sn:
                   if i.delievered == True:
                       print(i.product + "Has been delievered")
                       break
                   else:
                        print(i.product + "Has not been delievered")
       elif refrence == "add":
            information_gather()
       else:
           break
def prefill():
    """For testing im planning to randomly generate all values to be put into the form locations to work on accessing and editing information
    form within the storage list.
    Operates by generating an unique "Shipping Number" for each go around. Since models and manufactures are not being tracked, Its up to the Shipping
    Number for tracking purposes
    """
    item_gen_num = int(input("How many Items would you like generated?:"))
    track_list = []
    while item_gen_num != 0:
        char_count = 16
        combine_lst = []
        while char_count != 0:
            determine = random.randint(0, 1)
            if determine == 1:
                combine_lst.append(chr(random.randint(65, 90)))
            else:
                combine_lst.append(chr(random.randint(48, 57)))
            char_count -= 1
        item_gen_num -= 1
        track_list.append(''.join(combine_lst))
    print(track_list)
    for i in track_list:
        randctl = random.randint(0,2)
        if randctl == 0:
            package = Delivery("Fortinet 100D", 2, "SOmeNum", i, bool(random.getrandbits(1)), "T20200718.00012", "Deploy Room")
            shipping_items.append(package)
        elif randctl == 1:
            package = Delivery("Ruckus ZoneCommander", 2, "SOmeNum",i, bool(random.getrandbits(1)), "T20190905", "In Basement")
            shipping_items.append(package)
        elif randctl == 2:
            package = Delivery("Dell Optiplex 1050", 2, "SOmeNum", i, bool(random.getrandbits(1)), "T20201215.00054", "In Shipping" )
            shipping_items.append(package)
    print(shipping_items)
    check_to_recieve()

main()