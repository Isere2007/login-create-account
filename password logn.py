import PySimpleGUI as sg

def login(username, password):
    # Check if the username and password are correct
    if username == "admin" and password == "password":
        sg.popup("Login successful")
    else:
        sg.popup("Incorrect username or password")

def create_account(username, password):
    # Save the new user account
    with open("users.txt", "a") as f:
        f.write(f"{username}:{password}\n")
    sg.popup("Account created successfully")

# Define the layout for the login window
login_layout = [
    [sg.Text("Username"), sg.Input(key="username")],
    [sg.Text("Password"), sg.Input(key="password", password_char="*")],
    [sg.Button("Login"), sg.Button("Create Account")]
]

# Create the login window
login_window = sg.Window("Login System", login_layout)

# Event loop for the login window
while True:
    event, values = login_window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Login":
        login(values["username"], values["password"])
    elif event == "Create Account":
        # Define the layout for the create account window
        create_account_layout = [
            [sg.Text("Enter a new username and password:")],
            [sg.Text("Username"), sg.Input(key="new_username")],
            [sg.Text("Password"), sg.Input(key="new_password", password_char="*")],
            [sg.Button("Create Account")]
        ]
        # Create the create account window
        create_account_window = sg.Window("Create Account", create_account_layout)
        # Event loop for the create account window
        while True:
            event, values = create_account_window.read()
            if event == sg.WINDOW_CLOSED:
                break
            elif event == "Create Account":
                create_account(values["new_username"], values["new_password"])
                create_account_window.close()
login_window.close()
