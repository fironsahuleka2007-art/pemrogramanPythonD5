from Totalharga import hargatotal
from Inputbarang import harga
def Totalharga2(hargatotal):
    subtotal = 0
    
    for hargatotal in Totalharga:
        subtotal += hargatotal
    
    return subtotal
