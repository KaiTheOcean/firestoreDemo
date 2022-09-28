import pyrebase

# We are configering the firebase in the following step
# In here we are using web as for the python
firebaseConfig = {  
  "apiKey": "AIzaSyCuEl09GpElDXMCfR96iUAbaIUjuX5vDVI",
  "authDomain": "cloud-database-demo-f0db8.firebaseapp.com",
  "projectId": "cloud-database-demo-f0db8",
  "storageBucket": "cloud-database-demo-f0db8.appspot.com",
  "messagingSenderId": "119910820553",
  "databaseURL": "https://cloud-database-demo-f0db8.firebaseio.com",
  "appId": "1:119910820553:web:04a3b354d91806f2903b18",
  "measurementId": "G-00D39VZEYM"}

# Set up the firebase
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth() # This part allows us to access the authentication part of the firebase

def signup():
    print("Signing in......")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print("Successfully created the account!")
        ask = input("Do you want to login now?(y/n)")
        if ask == "y":
            login()
    except:
        print("Email already exists!")

def login():
    print("Log in......")
    email = input("Enter email: ")
    password = input("Enter password: ")
    try:
        login = auth.sign_in_with_email_and_password(email, password)
        print("Successfully logged in!")
    except: 
        print("Invalid email or password.")

teacher_password = input("What is your teacher's code to access this page?  ")
if teacher_password == "XA4756FBSUG234":
    is_new_user = input("Are you a new user?[y/n] ")
    if is_new_user.lower() == "y": 
        signup()
    elif is_new_user.lower() == "n":
        login()
    else: 
        print("You have entered the wrong information, please make sure to enter either y or n")