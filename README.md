# lcs_pcom7e_september_2022

### Requirements
```MacOS >= python3.10.4```
```Others >= python3.9.6```


### How to run application
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
Main interface of the application

1. Form to create and update contacts
 1.1 Name - required field
 1.2 Phone - required field
 1.3 Email - required field
2. Buttons to manipulate with records:
 2.1 Clear - clears form fields
 2.2 Create - after filling all fields in the form creates a record
 2.3 Update - updates selected record with values from form field
 2.4 Delete - deletes selected record
 2.5 Delete All - deletes all records
 2.6 List All - shows all records
3. Tree view of records
  Contains:
    ID - numeric identificator of a record
    Name - contact name
    Phone - contact phone
    Email - contact email
    Created - creation date of a record in iso format
    Updated - modifiaction date of a record in iso format
4. Search Input - Placeholder for search entry. Searched in name and phone fields
5. Search Button - Finds related records and updates tree view
6. Exit Button - closes application

<img width="1000" alt="Screenshot 2022-11-28 at 12 56 56 PM" src="https://user-images.githubusercontent.com/60176169/204245932-2c889868-5fb2-4716-9ec0-ce8ab339ea99.png">

### Sorting and Ordering
Sorting fields: Name, Email, Created, Updated
![Screenshot 2022-11-28 at 2 09 48 PM](https://user-images.githubusercontent.com/60176169/204245923-992e7b66-c331-4cce-b286-be662b26e9e8.png)

### Search
Searches in Name and Phone fields
<img width="897" alt="Screenshot 2022-11-28 at 2 32 04 PM" src="https://user-images.githubusercontent.com/60176169/204245946-fa9a94d5-3fa2-4ed9-9f43-d328194f12df.png">
