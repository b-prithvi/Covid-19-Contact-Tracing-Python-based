class Person: #Person class to model the individuals from the list
    def __init__(self,surname,first_name,gender,nid,town_village_city,age,comorbidities): #A constructor that accepts parameters to initialise all the attributes
        self.surname=surname
        self.first_name=first_name
        self.nid=nid
        self.town_village_city=town_village_city
        self.gender=gender
        self.age=age
        self.comorbidities=comorbidities
        
    #set and get methods for all attributes in the class
    def get_surname(self):
        return self.surname
    def set_surname(self,surname):
        self.surname=surname
    def get_first_name(self):
        return self.first_name
    def set_first_name(self,first_name):
        self.first_name=first_name
    def get_nid(self):
        return self.nid
    def set_nid(self,nid):
        self.nid=nid
    def get_town_village_city(self):
        return self.town_village_city
    def set_town_village_city(self,town_village_city):
        self.town_village_city=town_village_city
    def get_gender(self):
        return self.gender
    def set_gender(self,gender):
        self.gender=gender
    def get_age(self):
        return self.age
    def set_age(self,age):
        self.age=age
    def get_comorbidities(self):
        return self.comorbidities
    def set_comorbidities(self,comorbidities):
        self.comorbidities=comorbidities
        
    def displayInfo(self): #A special method: to be able to print out/display all the data for an instance of the class in a readable format
        return 'Surname:'+self.surname,'First_Name:'+self.first_name,'Gender:'+self.gender,'NID '+self.nid,'Town_Village_City:'+self.town_village_city,'Age:'+self.age,'Comorbidities:'+' '.join([str(elem) for elem in self.comorbidities])
