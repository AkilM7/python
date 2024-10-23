import sqlite3

# Password Validator
def is_valid_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not any(c.isupper() for c in password):
        return False, "Password must contain at least one uppercase letter."
    if not any(c.islower() for c in password):
        return False, "Password must contain at least one lowercase letter."
    if not any(c.isdigit() for c in password):
        return False, "Password must contain at least one digit."
    if not any(c in '!@#$%^&*(),.?":{}|<>' for c in password):
        return False, "Password must contain at least one special character."
    return True, "Password is valid."

# Store User in Database
def store_user(username, password):
    conn = sqlite3.connect('/home/akil/Documents/payilagam python/password validater.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("User registered successfully.")
    except sqlite3.IntegrityError:
        print("Username already exists.")
    conn.close()

# Verify User Login
def verify_user(username, password):
    conn = sqlite3.connect('/home/akil/Documents/payilagam python/password validater.db')
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    if result and result[0] == password:
        print("Login successful!")
    else:
        print("Invalid username or password.")
    conn.close()

# Main Program
password = input("Enter your password: ")
is_valid, message = is_valid_password(password)
print(message)

if is_valid:
    username = input("Enter your username: ")
    store_user(username, password)

login_username = input("Login - Enter your username: ")
login_password = input("Login - Enter your password: ")
verify_user(login_username, login_password)

