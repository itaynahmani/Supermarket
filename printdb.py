from persistence import *


def print_employees():
    print('Employees')
    for tmp in repo.employees.find_all('id'):
        print(tmp.__str__())

def print_suppliers():
    print('Suppliers')
    for sup in repo.suppliers.find_all('id'):
        print(sup.__str__())

def print_activities():
    print('Activities')
    for tmp in repo.activities.find_all('date'):
        print(tmp.__str__())

def print_products():
    print('Products')
    for tmp in repo.products.find_all('id'):
        print(tmp.__str__())

def print_branches():
    print('Branches')
    for tmp in repo.branches.find_all('id'):
        print(tmp.__str__())



def employeesReports():
    print('Employees report')
    for emp in repo.employees.find_all('name'):
        
        idDict = {'id':emp.branche}
        workLocation = repo.branches.find(**idDict)[0].location
        
        actIdDict = {'activator_id':emp.id}
        actList = repo.activities.find(**actIdDict)
        salesIncome = 0
        for act in actList:
            prodIdDict = {'id':act.product_id}
            productPrice = float(repo.products.find(**prodIdDict)[0].price)
            salesIncome += act.quantity * (-1) * productPrice

        print(emp.name+ " "+ str(emp.salary) + " " + workLocation + " " + str(salesIncome))


def activityReports():
    reports = repo.actRep()
    print("Activities report")
    for list in reports:
        print(list)
    

def main():
    print_activities()
    print_branches()
    print_employees()
    print_products()
    print_suppliers()
    print()
    employeesReports()
    print()
    activityReports()

if __name__ == '__main__':
    main()