# Registration-System-using-Django

This repository contains the code files required for a Registration System, including sign-up, login, logout functionalities, and a confirmation email feature. Users will receive a confirmation email to verify their account.

## Necessary Installations

You must have the following installed:

- **Python**
- **Django**

Additionally, make sure to:

- Run migrations
- Create a super user

## View Functions

1. **SignUpPage**  
   This view function renders the `signup.html` template, which contains the signup form.

2. **user_signup**  
   This function takes input from the user (username, first name, last name, email, and password) and creates a new user. After creating the user, a confirmation email is sent. Once the user confirms their account, they are redirected to the login page.

3. **Login_page**  
   This view function renders the `login.html` template, which contains the login form.

4. **user_login**  
   This function processes the login information entered by the user. If the user is authenticated, they are logged in and redirected to the home page.

5. **logout**  
   This function logs the user out of the system.
