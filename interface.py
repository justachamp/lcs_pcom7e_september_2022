import re
import tkinter as tk
import tkinter.messagebox as mb
import tkinter.ttk as ttk
from datetime import datetime as dt

from resource import Resource, ResourceCreateData

# regex for Email validation
regex = '^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\\.[a-zA-Z0-9-]+)*$'

# variable to know if any record was selected in tree view
contact_id = 0


class ContactBookApp(tk.Tk):
    """
        Contact Book GUI Application
    """

    def __init__(self, resource: Resource):
        self.resource = resource
        super().__init__()
        self.title("Contact Book")
        self.geometry("800x800")

        # register_labels
        self.title_label = tk.Label(self, text="Contact Book")
        self.name_label = tk.Label(self, text="Name:")
        self.phone_label = tk.Label(self, text="Phone Number:")
        self.email_label = tk.Label(self, text="Email:")
        self.search_label = tk.Label(self, text="Search:")

        # register_entries
        self.name_entry = tk.Entry(self)
        self.phone_entry = tk.Entry(self)
        self.email_entry = tk.Entry(self)
        self.search_entry = tk.Entry(self)

        # register_buttons
        self.create_button = tk.Button(self, text="Create", command=self.create_contact)
        self.update_button = tk.Button(self, text="Update", command=self.update_contact)
        self.delete_button = tk.Button(self, text="Delete", command=self.delete_contact)
        self.delete_all_button = tk.Button(self, text="Delete All", command=self.delete_all_contacts)
        self.clear_button = tk.Button(self, text="Clear", command=self.clear)
        self.list_all_button = tk.Button(self, text="List All", command=self.list_all)
        self.search_button = tk.Button(self, text="Search", command=self.search)
        self.exit_button = tk.Button(self, text="Exit", command=self.exit)

        # register_tree_view
        self.tree_view = ttk.Treeview(self, show="headings", height=5, columns=("#1", "#2", "#3", "#4", "#5", "6"))
        self.tree_view.heading('#1', text='ID', anchor='center')
        self.tree_view.column('#1', width=60, anchor='center', stretch=False)
        self.tree_view.heading('#2', text='Name', anchor='center',
                               command=lambda _col="#2": self.treeview_sort_column(self.tree_view, _col, False))
        self.tree_view.column('#2', width=10, anchor='center', stretch=True)
        self.tree_view.heading('#3', text='Phone', anchor='center')
        self.tree_view.column('#3', width=10, anchor='center', stretch=True)
        self.tree_view.heading('#4', text='Email', anchor='center',
                               command=lambda _col="#4": self.treeview_sort_column(self.tree_view, _col, False))
        self.tree_view.column('#4', width=10, anchor='center', stretch=True)
        self.tree_view.heading('#5', text='Created', anchor='center',
                               command=lambda _col="#5": self.treeview_sort_column(self.tree_view, _col, False))
        self.tree_view.column('#5', width=10, anchor='center', stretch=True)
        self.tree_view.heading('#6', text='Updated', anchor='center',
                               command=lambda _col="#6": self.treeview_sort_column(self.tree_view, _col, False))
        self.tree_view.column('#6', width=10, anchor='center', stretch=True)
        self.configure_tree_view()

        # place_elements
        self.title_label.place(x=280, y=30, height=27, width=300)
        self.name_label.place(x=175, y=70, height=23, width=100)
        self.phone_label.place(x=175, y=100, height=23, width=100)
        self.email_label.place(x=171, y=129, height=23, width=104)
        self.name_entry.place(x=277, y=72, height=21, width=186)
        self.phone_entry.place(x=277, y=100, height=21, width=186)
        self.email_entry.place(x=277, y=129, height=21, width=186)
        self.clear_button.place(x=175, y=245, height=25, width=76)
        self.create_button.place(x=290, y=245, height=25, width=76)
        self.update_button.place(x=370, y=245, height=25, width=76)
        self.delete_button.place(x=460, y=245, height=25, width=76)
        self.delete_all_button.place(x=548, y=245, height=25, width=76)
        self.list_all_button.place(x=630, y=245, height=25, width=76)
        self.search_label.place(x=210, y=558, height=23, width=65)
        self.search_entry.place(x=277, y=558, height=21, width=186)
        self.search_button.place(x=498, y=558, height=26, width=60)
        self.exit_button.place(x=320, y=610, height=31, width=60)
        self.tree_view.place(x=40, y=310, height=200, width=640)

        # list all stored records
        self.list_all()

    def configure_tree_view(self):
        vsb = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree_view.yview)
        vsb.place(x=40 + 640 + 1, y=310, height=180 + 20)
        self.tree_view.configure(yscrollcommand=vsb.set)
        hsb = ttk.Scrollbar(self, orient=tk.HORIZONTAL, command=self.tree_view.xview)
        hsb.place(x=40, y=310 + 200 + 1, width=620 + 20)
        self.tree_view.configure(xscrollcommand=hsb.set)
        self.tree_view.bind("<<TreeviewSelect>>", self.show_selected_record)

    def clear(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def exit(self):
        msg_box = mb.askquestion('Exit Application', 'Are you sure you want to exit the application', icon='warning')
        if msg_box == 'yes':
            self.destroy()

    def delete_contact(self):
        """Delete selected contact by retrieving record id from global vars"""
        global contact_id
        if not contact_id:
            mb.showinfo('Delete Contact', 'Please select contact first!', icon='warning')
            return
        msg_box = mb.askquestion('Delete Contact', 'Are you sure! you want to delete selected contact',
                                 icon='warning')
        if msg_box == 'yes':
            self.resource.delete(contact_id)
            mb.showinfo("Information", "Contact Deleted Successfully")
            self.list_all()
            self.clear()

    def delete_all_contacts(self):
        """Delete All contacts"""
        msg_box = mb.askquestion('Delete All Contacts', 'Are you sure! you want to delete all contacts',
                                 icon='warning')
        if msg_box == 'yes':
            self.resource.delete_all()
            mb.showinfo("Information", "Contacts Deleted Successfully")
            self.list_all()
            self.clear()

    def create_contact(self):
        """Create contact, validate entries"""
        name = self.name_entry.get()  # Retrieving entered name
        phone = self.phone_entry.get()  # Retrieving entered phone
        email = self.email_entry.get()  # Retrieving entered email
        # validating Entry Widgets
        if name == "":
            mb.showinfo('Information', "Please Enter Name")
            self.name_entry.focus_set()
            return
        if phone == "":
            mb.showinfo('Information', "Please Enter Phone Number")
            self.phone_entry.focus_set()
            return
        if not phone.isnumeric():
            mb.showinfo('Information', "Please Enter Valid Phone Number")
            self.phone_entry.focus_set()
            return
        if email == "":
            mb.showinfo('Information', "Please Enter Contact Number")
            self.email_entry.focus_set()
            return
        if not self.validate_email(email):
            mb.showinfo('Information', "Please Enter Valid Email Address")
            self.phone_entry.focus_set()
            return
        data = ResourceCreateData(
            name=name, phone=int(phone), email=email, created=dt.now().isoformat()
        )
        self.resource.create(data)
        mb.showinfo('Information', "Contact Created Successfully")
        self.list_all()

    def search(self):
        """Search for a contact in Name and Phone fields"""
        search_text = self.search_entry.get()  # Retrieving entered first name
        print(search_text)
        if search_text == "":
            mb.showinfo('Information', "Please Enter Contact Name or Phone Number")
            self.search_entry.focus_set()
            return
        self.tree_view.delete(*self.tree_view.get_children())  # clears the treeview tree_view
        if search_text.isdigit():
            data = self.resource.search_in_phone_number(list(self.resource.data.values()), search_text)
        else:
            data = self.resource.search_in_names(list(self.resource.data.values()), search_text)

        for datum in data:
            c_id = datum['id']
            name = datum['name']
            phone = datum['phone']
            email = datum['email']
            created = datum['created']
            updated = datum.get('updated', '')
            self.tree_view.insert("", 'end', text=str(c_id), values=(c_id, name, phone, email, created, updated))

    def show_selected_record(self, _):
        """Fill form with the data from selected record"""
        self.clear()
        for selection in self.tree_view.selection():
            item = self.tree_view.item(selection)
            global contact_id
            contact_id, name, phone, email, created, updated = item["values"][0:6]
            self.name_entry.insert(0, name)
            self.phone_entry.insert(0, phone)
            self.email_entry.insert(0, email)
            return contact_id

    def update_contact(self):
        """Update contact by retrieving record id from global vars"""
        global contact_id
        if not contact_id:
            mb.showinfo('Update Contact', 'Please select contact first!', icon='warning')
            return

        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if not self.validate_email(email):
            mb.showinfo('Information', "Please Enter Valid Email Address")
            self.phone_entry.focus_set()
            return
        if not phone.isnumeric():
            mb.showinfo('Information', "Please Enter Valid Phone Number")
            self.phone_entry.focus_set()
            return

        _, data = self.resource.get(contact_id)
        data['name'] = name
        data['phone'] = phone
        data['email'] = email
        data['updated'] = dt.now().isoformat()
        self.resource.update(data)
        mb.showinfo("Info", "Selected Contact Updated Successfully ")
        self.list_all()

    def list_all(self):
        """List all records"""
        self.tree_view.delete(*self.tree_view.get_children())  # clears the treeview tree_view
        for datum in self.resource.data.values():
            c_id = datum['id']
            name = datum['name']
            phone = datum['phone']
            email = datum['email']
            created = datum['created']
            updated = datum.get('updated', '')
            self.tree_view.insert("", 'end', text=c_id, values=(c_id, name, phone, email, created, updated))

    @staticmethod
    def validate_email(email):
        """ Validate email address"""
        if re.search(regex, email):
            return True
        return False

    @staticmethod
    def treeview_sort_column(tree_view, column, reverse):
        """Sort records inside treeview"""
        columns = {
            "#1": "ID",
            "#2": "Name",
            "#3": "Phone",
            "#4": "Email",
            "#5": "Created",
            "#6": "Updated",
        }

        lst = [(tree_view.set(k, column), k) for k in tree_view.get_children('')]
        lst.sort(reverse=reverse)

        # rearrange items in sorted positions
        for index, (val, k) in enumerate(lst):
            tree_view.move(k, '', index)

        # reverse sort next time
        arrow = u'\u2191' if reverse else u'\u2193'
        tree_view.heading(column, text=columns[column] + arrow,
                          command=lambda _col=column: ContactBookApp.treeview_sort_column(tree_view, _col, not reverse))


if __name__ == "__main__":
    # Run application
    app = ContactBookApp(Resource())
    app.mainloop()
