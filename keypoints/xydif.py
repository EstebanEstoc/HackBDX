
from math import *

def xydif(tabinit,tab):

    diffcrit = 160
    deltacrit = 40
    alpha1 = 1
    alpha17 = 1
    alpha9 = 3
    alphaD = 1.4

    norme1 = sqrt((tabinit[0]-tab[0])**2 + (tabinit[1]-tab[1])**2)
    norme17 = sqrt((tabinit[2]-tab[2])**2 + (tabinit[3]-tab[3])**2)
    norme9 = sqrt((tabinit[4]-tab[4])**2 + (tabinit[5]-tab[5])**2)
    deltaD = abs(tabinit[6]-tab[6])
    
    form1 = alpha1 * norme1 + alpha17 * norme17 + alpha9 * norme9 + alphaD*deltaD
    form2 = alphaD*deltaD
    if form1 > diffcrit:
        ret1 = False
    else:
        ret1 =  True 

    if (tab[6] > (alphaD*tabinit[6])):
        ret2 = False
    else:
        ret2 =  True 
    return ret1,ret2
