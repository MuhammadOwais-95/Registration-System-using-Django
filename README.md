# Registration-System-using-Django
This repository contain the code files required for a Registration System i.e sign up ,login , logout and additionally it has the concept of confirmation email that means that the user will receive the email for confirmation of his/her account.
# necessery installations
##you must have the following things installed
###python
###django
###run miagrations 
###created a super user 
#Views functions
1 SignUpPage ==> it will only render the signup.html (which contain the signup form) 
2 user_signup ==> it will get the input from the user i.e username, first name ,last name ,email, and password and then create the user
                  and then the user will receive the confirmation email. after confirmation the user will be redirected to login page
3 Login_page ==> it will only render the login.html (contain the login form)
4 user_login ==> it will receive the login information entered and the if the user is athunticated then he/she will be logged in and 
                 the user will be redirectd to home page.
5 logout ==> it will simply logout the user from data base

                      
                          
