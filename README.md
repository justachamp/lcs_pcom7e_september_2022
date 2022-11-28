# lcs_pcom7e_september_2022


### Implementation
The application is built on Python's built-in library Tkinter. 
Form Fields:  
Name - the name of a contact, string, not unique, can have multiple occurrences 
Phone - phone number of a contact, numeric, not unique, can have multiple occurrences 
Email - email address of a contact, string, not unique, can have multiple occurrences 
There are buttons for manipulating data: create, read, update, delete, and additional methods for searching and sorting records 
1. Create: 
In order to create a record the form should be filled with valid data, after the data is handled by the `create_contact()` method   
The `create_contact()` method creates a record and shows an informational message box stating the success of the operation. 
Then the newly created record should appear in the tree view
2. Update: 
To update a contact, first, it should be selected in tree view then the form will be automatically filled with the data of the selected contact. 
After making relevant changes pressing the Update button invokes `update_contact()`, which in turn updates the record in the storage file
3. Delete: 
To update a contact, first, it should be selected in tree view then after pressing the Delete button `delete_contact()` method is invoked,
which in turn shows a warning message box to get confirmation of the desired action and when it is received it deletes the selected record in the storage file
4. Delete All:
When the button is pressed `delete_all_contacts()` method is invoked,
which in turn shows a warning message box to get confirmation of the desired action and when it is received it deletes all records in the storage file
5. Clear: 
invokes the `clear()` method, which clears form fields
6. List All: 
invokes the `list_all()` method, which drops sorting, ordering, search and gets all records in the storage file, and updates the tree view with all records
7. Search: 
After filing some data in Search input and Pressing the Search button `search()` method is invoked.
If input data is numeric then the search is done in the phone field or else in the name field. The tree view is updated with the output records
8. Exit: 
The `exit()` method asks for confirmation when it is received the application process is destroyed
9. To store and manipulate data in the backside of the application used the instance of Resource class, which stores data in JSON format in the local file name resources.json   
10. Added user entry validations for Phone and Email fields. The phone is checked to be numeric and the Email is validated via the regex pattern   
11. Written tests to check the algorithm. It can be found in the tests.py file. To run tests execute the following command `python tests.py`   
The output should be printed in the console whether all tests passed or exception traceback is printed in case of an error



### Testing Strategy
1. To test the application there were written tests, which covered nearly all methods of Resource and ResourceMeta classes 
1.1 test_create_resource method tests functionality to create a contact 
1.2 test_get_resource method tests functionality to retrieve a contact by id  
1.3 test_update_resource method tests functionality to update a contact by id 
1.4 test_delete_by_id method tests functionality to delete a contact by id 
1.6 test_delete_all method tests functionality to delete all contacts 
1.7 test_delete_all method tests functionality to delete all contacts 
1.8 test_search method tests functionality to search for input string among all contacts in Name and Phone fields    
1.9 test_all method runs all the above methods in a specific order to test the whole functionality (end-to-end testing)  
2. Manual Testing was done to validate the correctness of the algorithm of the application via the GUI interface 
2.1 Created Contact with the following data: Name - Contact, Phone - 7412313, Email - c@email.com -> SUCCESS 
2.2 Created Contact with the following data: Name - Person, Phone - 7412313, Email - p@email.com -> SUCCESS 
2.3 Tried to create Contact with the following data: Name - Person, Phone - ABC, Email - p@email.com -> FAILED TO CREATE 
2.4 Tried to create Contact with the following data: Name - Person, Phone - 7412313, Email - p@ -> FAILED TO CREATE 
2.5 Selected Contact 'Person' then updated the phone to 1234556 -> SUCCESS 
2.6 Searched for 'Con', received output is only one record which has 'Con' in Name field -> SUCCESS  
2.7 Applied Sorting via TreeView on Name, received output of two records, first is 'Contact', the second is 'Person' -> SUCCESS  
2.8 Applied Sorting via TreeView on Name again, changed the order to descending, received output of two records, first is 'Person', the second is 'Contact' -> SUCCESS  
2.9 Select and delete contact 'Person'  -> SUCCESS 
2.10 Delete All Contacts -> SUCCESS 



### Requirements
```MacOS >= python3.10.4```
```Others >= python3.9.6```


### How to run the application
Unix
```
  python -m venv venv
 .\venv\bin\activate
 python interface.py
```
Others
```
 python -m venv venv
 .\venv\Scripts\activate
 python interface.py
```

### Interface
The main interface of the application 

1. Form to create and update contacts 
1.1 Name - required field 
1.2 Phone - required field 
1.3 Email - required field 
2. Buttons to manipulate with records: 
2.1 Clear - clears form fields 
2.2 Create - after filling all fields in the form create a record 
2.3 Update - updates selected record with values from the form field 
2.4 Delete - deletes selected record 
2.5 Delete All - deletes all records 
2.6 List All - shows all records 
3. Tree view of records 
 Contains: 
   ID - numeric identification of a record 
   Name - contact name 
   Phone - contact phone 
   Email - contact email 
   Created - creation date of a record in iso format 
   Updated - modification date of a record in iso format 
4. Search Input - Placeholder for search entry. Searched in name and phone fields 
5. Search Button - Finds related records and updates tree view 
6. Exit Button - closes the application 

<img width="1000" alt="Screenshot 2022-11-28 at 12 56 56 PM" src="https://user-images.githubusercontent.com/60176169/204245932-2c889868-5fb2-4716-9ec0-ce8ab339ea99.png">

### Sorting and Ordering 
Sorting fields: Name, Email, Created, Updated   
![Screenshot 2022-11-28 at 2 09 48 PM](https://user-images.githubusercontent.com/60176169/204245923-992e7b66-c331-4cce-b286-be662b26e9e8.png)

### Search
Searches in Name and Phone fields  
<img width="897" alt="Screenshot 2022-11-28 at 2 32 04 PM" src="https://user-images.githubusercontent.com/60176169/204245946-fa9a94d5-3fa2-4ed9-9f43-d328194f12df.png">
