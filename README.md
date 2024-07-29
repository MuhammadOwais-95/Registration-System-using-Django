# Registration-System-using-Django

This repository contains the code files required for a Registration System, including sign-up, login, logout functionalities, and a confirmation email feature. Users will receive a confirmation email to verify their account.

## Necessary Installations

To run this project, you need to have the following installed:

- **Python**
- **Django**

Additionally, make sure to:

- Run migrations
- Create a super user

## View Functions

1. **SignUpPage**  
   This view function renders the `signup.html` template, which contains the signup form.

2. **user_signup**  
   This function takes input from the user (username, first name, last name, email, and password) and creates a new user. After creating the user, a confirmation email is sent to the user. Once confirmed, the user is redirected to the login page.
