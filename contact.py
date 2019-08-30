import pyperclip

class Contact:
 """
 Class that generates new instances of contacts.
 """
 contact_list = [] # Empty contact list

 def __init__(self,first_name,last_name,number,email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
 # create a save contact attribute
 def save_contact(self):

        '''
        save_contact method saves contact objects into contact_list
        '''

        Contact.contact_list.append(self)
   # create a delete contact attribute 
 def delete_contact(self):

        '''
        delete_contact method deletes a saved contact from the contact_list
        '''

        Contact.contact_list.remove(self) # uses the remove method to remote contact from the contact_list
 # create a find_by_number class
 @classmethod # decorator - they allow one to make simple modifications to callable objects
 def find_by_number(cls,number): # cls refered to the entire class and does not need to be passed when we call the entire method
     '''
     Method that takes in a number and returns a contact
     that matches that number. 

     Args:
        number: Phone number to search for
    Returns :
        Contact of person that matches the number.
     '''
     for contact in cls.contact_list:
        if contact.phone_number == number:
            return contact
 @classmethod
 def contact_exist(cls,number):
        '''
        Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for contact in cls.contact_list:
            if contact.phone_number == number:
                    return True

        return False
 @classmethod
 def display_contacts(cls):
     '''
     method that returns the contact list
     '''
     return cls.contact_list
 @classmethod
 def copy_email(cls,number):
     contact_found = Contact.find_by_number(number)
     pyperclip.copy(contact_found.email)
    # pyperclip.copy() method allows us to copy the contact to the machine's keyboard
    
   #self is a special keyword in python could be likened to this in  js
    #doc string removed for simplicity