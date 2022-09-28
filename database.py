import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Access the serviceAccountKey
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

def add_data():
    '''For teacher to add new students' information in'''

    print("Enter the following information for the new studnet")

    # Get the information from the teacher and insert data
    name = input("What is the name of this studnet? ")
    id = int(input("What is the ID for this student? "))
    age = int(input("What is the age of this student? "))
    contact_info = int(input("What is the phone number of this studnet? "))
    address = input("What is the address of this student? ")
    result = db.collection("StudentsWithID").document(name).get()

    # If the student is currently in the databse
    if result.exists:
        print("This ID is being using now")
        return 
    
    # Else insert the data in
    student = {"Name": name, "ID": id, "Age": age, "Contact_info": contact_info, "Address": address}
    db.collection("StudentsWithID").document(name).set(student)
    print("Successfully added the new student!")

def modify_data():
    '''For teacher to modify the current existing students' data'''

    # Ask the teacher for which action to take, either update or delete
    action = input("Update data or delete data? (update\delete) ")

    # Action with update
    if action.lower() == "update":
        name = input("What is the name of this studnet? ")
        id = int(input("What is the ID for this student? "))
        age = int(input("What is the age of this student? "))
        contact_info = int(input("What is the phone number of this studnet? "))
        address = input("What is the address of this student? ")
        db.collection("StudentsWithID").document(name).update({"ID": id})
        db.collection("StudentsWithID").document(name).update({"Age": age})
        db.collection("StudentsWithID").document(name).update({"Contact_info": contact_info})
        db.collection("StudentsWithID").document(name).update({"Address": address})
        print("Successfully updated this student's information")

    # Action with delete
    elif action.lower() == "delete":
        document = input("What is the student's name which you wnat to delete? ")
        db.collection("StudentsWithID").document(document).delete()
        print("Successfully deleted this student's information")

    # Action is neither update nor delete
    else:
        print("You have entered the wrong information, please make sure to \
            enter either 'update' or 'delete'")

def retrive_data():
    '''For teacher to retrive the existing students' data either with update or delete'''

    retrive = input("Do you know which student's you'd like to see? [y/n] ")

    # Retrive a specific data
    if retrive.lower() == "y":
        name = str(input("what is the name of that student? "))
        result = db.collection("StudentsWithID").document(name).get()
        if result.exists:
            print(result.to_dict())

    # Retrive all students for teach to see
    elif retrive.lower() == "n":
        print("All the students' information: ")
        print()
        docs = db.collection("StudentsWithID").get()
        for doc in docs:
            print(doc.to_dict())

def display_menu():
    '''Display a user menu for teacher to use'''

    print("Select Query")
    print("1) Show Students")        
    print("2) Add Students")
    print("3) Modify Students")
    choice = int(input("> "))
    print()
    if choice == 1:
        retrive_data()
    elif choice == 2:
        add_data()
    elif choice == 3:
        modify_data()
    else: 
        print("You have entered the wrong command")

display_menu()

# Below are some basic inserts, updates 

# Add collection and insert values in it with auto IDs
# Student1 stores the one student's info 
# and the collection name is Students
# student1 = {"ID": 1, "Name": "Kai", "Age": 23, "Contact_info": 2089735376, "Address": "Rexburg"}
# db.collection("Students").add(student1)
# student2 = {"ID": 2, "Name": "A", "Age": 22, "Contact_info": 2085742854, "Address": "New York"}
# db.collection("Students").add(student2)
# student3 = {"ID": 3, "Name": "B", "Age": 22, "Contact_info": 2087241234, "Address": "LA"}
# db.collection("Students").add(student3)
# student4 = {"ID": 4, "Name": "C", "Age": 21, "Contact_info": 2082341209, "Address": "Rexburg"}
# db.collection("Students").add(student4)
# student5 = {"ID": 5, "Name": "D", "Age": 29, "Contact_info": 2089075980, "Address": "Rexburg"}
# db.collection("Students").add(student5)

# Set documents with known IDs
# If you want a auto ID, then you can clear out everything within the document()
# student1 = {"ID": 1, "Name": "Kai", "Age": 23, "Contact_info": 2089735376, "Address": "Rexburg"}
# db.collection("StudentsWithID").document("Kai").set(student1)
# student2 = {"ID": 2, "Name": "A", "Age": 22, "Contact_info": 2085742854, "Address": "New York"}
# db.collection("StudentsWithID").document("A").set(student2)
# student3 = {"ID": 3, "Name": "B", "Age": 22, "Contact_info": 2087241234, "Address": "LA"}
# db.collection("StudentsWithID").document("B").set(student3)
# student4 = {"ID": 4, "Name": "C", "Age": 21, "Contact_info": 2082341209, "Address": "Rexburg"}
# db.collection("StudentsWithID").document("C").set(student4)
# student5 = {"ID": 5, "Name": "D", "Age": 29, "Contact_info": 2089075980, "Address": "Rexburg"}
# db.collection("StudentsWithID").document("D").set(student5)

# Reading data from the cloud databse application 
# Getting the document with the known ID 
# result = db.collection("StudentsWithID").document("A").get()
# if result.exists:
#     # to_dict() is a function for us to print it in a dic format
#     print(result.to_dict())

# Get all documents in a collection
# docs = db.collection("StudentsWithID").get()
# for doc in docs:
#     print(doc.to_dict())

# Querying 
# Equal 
# We can also use ==, !=, <, >, <=, >=
# docs = db.collection("StudentsWithID").where("Age", ">", 22).get()
# for doc in docs:
#     print(doc.to_dict())

# Compare strings
# docs = db.collection("StudentsWithID").where("Address", "==", "Rexburg").get()
# for doc in docs:
#     print(doc.to_dict())

# Update data in the cloud database with the known key
# For strings would be "Name": "kaidi"
# db.collection("StudentsWithID").document("Kai").update({"Age": 24})
# result = db.collection("StudentsWithID").document("Kai").get()
# if result.exists:
#     print(result.to_dict())

# Delete data from cloud databse with the known key
# db.collection("StudentsWithID").document("A").delete()

# Delete with query 
# docs = db.collection("StudentsWithID").where("Age", ">=", 25).get()
# for doc in docs:
    
#     # Svae the key and store it for later to find the document
#     key = doc.id
#     db.collection("StudentsWithID").document(key).delete()
