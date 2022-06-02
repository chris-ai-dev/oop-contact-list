class ContactList:
    
    
    #init constructor
    def __init__(self, name, group_contacts):
        self.name = name
        self.group_contacts = group_contacts

    #instance method should add new contact to the list, while keeping the list sorted
    def add_contact(self,name,number):
        newContact = {}
        newContact['name'] = name
        newContact['number'] = number
        self.group_contacts.append(newContact)
    
    #instance method should remove a contact from the list by name
    def remove_contact(self,name):
        for person in self.group_contacts:
            if person['name'] == name:
                self.group_contacts.remove(person) 
            
    
    #should accept another contact list as an argument, and then return a new list of dictionaries to indicate all the contacts that appear in both lists (exact same name and phone number).
    def find_shared_contacts(self, another_contactList):
        common_contacts = []
        for person in self.group_contacts:
            if person in another_contactList.group_contacts:
                common_contacts.append(person)
        return ContactList("Network contacts", common_contacts)        

friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList('My Friends', friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

my_friends_list.add_contact("Kevin","555-5555")
print(my_friends_list.group_contacts)

my_friends_list.remove_contact('Kevin')
print(my_friends_list.group_contacts)

new = my_friends_list.find_shared_contacts(my_work_buddies)
print(new.group_contacts)

#ContactList.test()

# friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
# friends_i_work_with should be: [{'name':'Alice','number':'867-5309'}]