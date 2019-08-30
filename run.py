#!/usr/bin/env python3.6
from contact import Contact
# creating a contact
def create_contact(fname,lname,phone,email):
    '''
    Function to create new contact
    '''
    new_contact = Contact(fname,lname,phone,email)
    return new_contact
# saving contacts
def save_contacts(contact):
    '''
    Function to save contact
    '''
    contact.save_contacts()
# delete contact
def del_contact(contact):
    '''
    function to delete contact
    '''
    contact.delete_contact()
# finding a contact
def find_contact(number):
    '''
    Function that finds a contact by number and returns the 
    contact
    '''
    return Contact.find_by_number(number)
# check if a contact exists
def checking_if_contact_exists(number):
    '''
    function to check if a contact exists with the number and 
    return a boolean
    '''
    return Contact.contact_exist(number)
# displaying all contacts
def display_contacts():
    '''
    function that returns all saved contacts
    '''
    return Contact.display_contacts()
