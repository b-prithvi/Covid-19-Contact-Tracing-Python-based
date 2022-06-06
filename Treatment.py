import Person
import pandas as pd
from queue import Queue
from queue import LifoQueue

person_group=[] #globally accessible list

def main(): #main() function consisting of several function calls to retrieve and process data
    global person_group
    data_reader()
    print('Data extracted from file:\n')
    for prithvi_obj in person_group:#Once all objects have been added to the list, an iteration is used to print the list
        print(*prithvi_obj.displayInfo())
    
    senior_citizens_group = one_year_later()#an updated list of individuals after the increment.
    print('*************************************************************************************************************')
    print('\nData with age updated by 1 year:\n')
    for prithvi_obj in senior_citizens_group:#display the updated list of individuals after the increment
        print(*prithvi_obj.displayInfo())
    people_by_location(senior_citizens_group)#show how many individuals come from each village/town/city
    
    potential_group = search_potential_infected(senior_citizens_group,"Rose Belle")#identifies all individuals living in Rose Belle, prints their details
    print('\nList of individuals from Rose Belle:\n')
    for prithvi_obj in potential_group:
        print(*prithvi_obj.displayInfo())
        
    kavi_sort_list = bubble_sort(potential_group)#sorts the list potential_group by surname,
    print('\nList sorted by surname:\n')
    for prithvi_obj in kavi_sort_list:#display sorted list potential_group by surname
        print(*prithvi_obj.displayInfo())
    
    if binary_search_by_surname(kavi_sort_list, "Losiko") == -1: #binary search algorithm to verify whether any individual by the surname
        #If not present, the function returns -1
        print("\nInfected Individual NOT Found in the list\n")
    else:
        print("\nInfected Individual Found in the list\n")
        bus= test_potential_group(kavi_sort_list)
        print('\nArrival at quarantine facility:\n')
        arrival_at_quarantine(bus) #Remove each object from the stack bus


def data_reader(): # Read the file rawdata.txt, instantiate a Person object for each individual and store the object in the globally accessible list person_group.
    global person_group
    file = open("rawdata.txt","r")
    next(file) #skip the first line
    rows = [r.strip().split(',') for r in file.readlines()] #store in list of lists
    for line in rows: #comorbidities is stored as an arrayList of type string
        line[6]=list(line[6].split(';'))
    person_group = [Person.Person(*row) for row in rows] #instantiate a Person object for each individual and store the object in the globally accessible list


def one_year_later(): #To increment all the individuals' age by 1.
    global person_group
    for prithvi_obj in person_group: #calling set_age funtion of each of object and set the age
        prithvi_obj.set_age(str(int(prithvi_obj.get_age())+1))
    return person_group


def people_by_location(senior_citizens_group): # Iterates through the group and fill a dictionary to show how many individuals come from each village/town/city
    df = pd.DataFrame([x.displayInfo() for x in senior_citizens_group], columns = ['Surname','FirstName','Gender','NID','Town_Village_City','Age','Comorbidities']) #create a dataframe
    Location_Statistics=df.groupby(['Town_Village_City']).size().reset_index(name='counts') #group by city and get the count of each city
    l1=Location_Statistics['Town_Village_City'] #create two list and print in a appropriate way
    l2=Location_Statistics['counts']
    print('*************************************************************************************************************\n')
    print('Location Statistics:'+str(dict(zip(l1,l2))))
    print('\n*************************************************************************************************************')


def search_potential_infected(senior_citizens_group,city):#Takes a list and a string as parameters, iterates through the list, identifies all individuals living in Rose Belle,
#prints their details on screen, adds them to karan_tempo_list ordinary list which is returned.
    karan_tempo_list=[]                                                                                                                                   
    for prithvi_obj in senior_citizens_group:
        if prithvi_obj.get_town_village_city()==city:#binary search
            karan_tempo_list.append(prithvi_obj)
    return karan_tempo_list                                                                                                                                         


def bubble_sort(potential_group):#sorts the list potential_group by surname, the sorted list is printed and returned.
  for passnum in range(len(potential_group)-1, 0, -1):
     for i in range(passnum):
        if str(potential_group[i].displayInfo()[0]) > str(potential_group[i+1].displayInfo()[0]):
            karan_tempo_list = potential_group[i]
            potential_group[i] = potential_group[i+1]
            potential_group[i+1] = karan_tempo_list                                                                                                                                         
  return potential_group


def binary_search_by_surname(kavi_sort_list, surname):#Conduct a search using the binary search algorithm to verify whether any individual by the surname
    for prithvi_obj in kavi_sort_list:
        if prithvi_obj.get_surname()==surname:#binary search
            return kavi_sort_list.index(prithvi_obj)
    return -1


def test_potential_group(kavi_sort_list):#get the list of persons tested and embarked on bus
    q=Queue()
    bus_to_quarantine = LifoQueue()
    for prithvi_obj in kavi_sort_list:#Add all objects from the kavi_sort_list list to the locally declared Queue
        q.put(prithvi_obj)
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
        
