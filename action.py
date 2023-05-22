from persistence import *

import sys

def main(args ):
    inputfilename : str = args[1]
    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            add_activity(splittedline)


def add_activity(splittedline):
    pID = splittedline[0]
    keyvals = {'id':pID}
    
    currentProductQuantity = repo.products.find(**keyvals)[0].quantity
    additionProdQuan = int(splittedline[1])
    if(additionProdQuan > 0 or (additionProdQuan < 0 and (currentProductQuantity > (-1)*additionProdQuan))):
        repo.activities.insert(Activitie(*splittedline))
        newQuantity = (additionProdQuan + currentProductQuantity)
        repo.products.update({'quantity':newQuantity}, {'id':pID})

if __name__ == '__main__':
    main(sys.argv)