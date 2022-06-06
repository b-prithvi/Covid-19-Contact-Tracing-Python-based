import Person
import pandas as pd
from queue import Queue
from queue import LifoQueue

person_group=[] #globally accessible list
def main(): #main() function consisting of several function calls to retrieve and process data
    global person_group
    data_reader()
    print('Data extracted from file:\n')
    for obj in person_group:#Once all objects have been added to the list, an iteration is used to print the list
        print(*obj.displayInfo())
    
    older_person_group=one_year_later()#an updated list of individuals after the increment.
    print('*************************************************************************************************************')
    print('\nData with age updated by 1 year:\n')
    for obj in older_person_group:#display the updated list of individuals after the increment
        print(*obj.displayInfo())
    people_by_location(older_person_group)#show how many individuals come from each village/town/city
    
    potential_group = search_potential_infected(older_person_group,"Rose Belle")#identifies all individuals living in Rose Belle, prints their details
    print('\nList of individuals from Rose Belle:\n')
    for obj in potential_group:
        print(*obj.displayInfo())
        
    sorted_by_surname =bubble_sort(potential_group)#sorts the list potential_group by surname,
    print('\nList sorted by surname:\n')
    for obj in sorted_by_surname:#display sorted list potential_group by surname
        print(*obj.displayInfo())
    
    if binary_search_by_surname(sorted_by_surname, "Losiko") == -1: #the binary search algorithm to verify whether any individual by the surname
        #If not present, the function returns -1
        print("\nInfected Individual NOT Found in the list\n")
    else:
        print("\nInfected Individual Found in the list\n")
        bus= test_potential_group(sorted_by_surname)
        print('\nArrival at quarantine facility:\n')
        arrival_at_quarantine(bus)#Remove each object from the stack bus


def data_reader():#To read the file rawdata.txt ,instantiate a Person object for each individual and store the object in the globally accessible list person_group.
    global person_group
    file = open("rawdata.txt","r")#open the file to read
    next(file)#skip the first line
    rows = [r.strip().split(',') for r in file.readlines()]#store in list of lists
    for line in rows:#comorbidities is stored as an arrayList of type string
        line[6]=list(line[6].split(';'))
    person_group = [Person.Person(*row) for row in rows]#instantiate a Person object for each individual and store the object in the globally accessible list

def one_year_later():#Since the data is being analysed one year after it was collected, all the individuals' age will have to be incremented by 1.
    global person_group
    for obj in person_group:#calling the set_age funtion of each of object and set the age
        obj.set_age(str(int(obj.get_age())+1))
    return person_group

def people_by_location(older_person_group):#This function iterates through the group and fill a dictionary to show how many individuals come from each village/town/city
    df = pd.DataFrame([x.displayInfo() for x in older_person_group], columns = ['Surname','FirstName','Gender','NID','Town_Village_City','Age','Comorbidities'])#creat a dataframe
    Location_Statistics=df.groupby(['Town_Village_City']).size().reset_index(name='counts')#group by city and get the count of each city
    l1=Location_Statistics['Town_Village_City']#create two list and print in a appropriate way
    l2=Location_Statistics['counts']
    print('*************************************************************************************************************\n')
    print('Location Statistics:'+str(dict(zip(l1,l2))))
    print('\n*************************************************************************************************************')
def search_potential_infected(older_person_group,city):#Takes a list and a string as parameters, iterates through the list, identifies all individuals living in Rose Belle,
    #prints their details on screen, adds them to a temporary list which is returned.
    temp=[]#tempory list
    for obj in older_person_group:
        if obj.get_town_village_city()==city:#binary search
            temp.append(obj)
    return temp

def bubble_sort(potential_group):#sorts the list potential_group by surname, the sorted list is printed and returned.
  for passnum in range(len(potential_group)-1, 0, -1):
     for i in range(passnum):
        if str(potential_group[i].displayInfo()[0]) > str(potential_group[i+1].displayInfo()[0]):
            temp = potential_group[i]
            potential_group[i] = potential_group[i+1]
            potential_group[i+1] = temp
  return potential_group

def binary_search_by_surname(sorted_by_surname, surname):#Conduct a search using the binary search algorithm to verify whether any individual by the surname
    for obj in sorted_by_surname:
        if obj.get_surname()==surname:#binary search
            return sorted_by_surname.index(obj)
    return -1

def test_potential_group(sorted_by_surname):#get the list of persons tested and embarked on bus
    q=Queue()
    bus_to_quarantine = LifoQueue()
    for obj in sorted_by_surname:#Add all objects from the sorted_by_surname list to the locally declared Queue
        q.put(obj)
    for x in range(q.qsize()):#all those suffering from comorbidities and are aged 70 or above are added to stack
        person=q.get()
        if ' '.join([str(elem) for elem in person.get_comorbidities()])!='none' and int(person.get_age())>=70:
            bus_to_quarantine.put(person)
            print(person.get_nid()," has been tested and embarked on bus")
    return bus_to_quarantine#return the stack

def arrival_at_quarantine(bus):#Remove each object from the stack bus and display
    while(not bus==[]):
        print(bus.get().displayInfo(),' has disembarked and been quarantined')
if __name__ == '__main__':
    main()
        
