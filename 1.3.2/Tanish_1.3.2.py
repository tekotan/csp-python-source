def add_tip(total, tip_percent): 
    '''Return the total amount including tip'''
    tip = tip_percent*total
    return total + tip
def hyp(leg_a, leg_b):
    """ Return the hypotenuse of a triangle with legs leg_a and leg_b"""
    return (leg_a**2 + leg_b**2)**0.5
def mean(*list_numbers):
    total = 0
    for num in list_numbers:
        total+=num
    return total/float(len(list_numbers))
def perimeter(base,height):
    return 2*(base+height)
#1.3.2 Function Test
print (add_tip(20,0.15))
print (add_tip(30,0.15))
print (hyp(3,4))
print (mean(3,4,7))
print (perimeter(3,4))