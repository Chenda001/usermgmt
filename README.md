
**STEP 1: PROJECT SET UP**

  I started by by setting up my project by by the name "user-mgmt" and create an app and named it 'accounts'. 
  I then added added it in the installed apps in the user-mgmt/setting.py ensure that django recognises the app.
  
<img width="276" height="114" alt="Screenshot 2025-07-07 150955" src="https://github.com/user-attachments/assets/1346d570-0da6-4c39-847f-ed22b4c6f238" />


**STEP 2: User Registration.**

This project includes a simple user authentication system using Django's built-in tools.

it What’s Implemented
User Registration
Uses Django’s UserCreationForm
Allows users to register with a username, name, phone and password
Accessible at: /accounts/register/

<img width="828" height="549" alt="Screenshot 2025-07-11 140702" src="https://github.com/user-attachments/assets/f3253210-331f-4e04-a8c2-73db633b3624" />


_User Login_
Uses Django’s built-in LoginView
Allows registered users to log in securely
Accessible at: /accounts/login/

<img width="472" height="112" alt="Screenshot 2025-07-07 193739" src="https://github.com/user-attachments/assets/cda160e5-5aed-4cbe-b6a0-c03d684c726a" />




**Redirection**
Upon successful login, users are redirected to the home page (/)



**STEP 3: Email Verification (Custom Django Feature)
Description**

This project implements email verification as part of the user registration process. After a user registers, a confirmation email is sent with a verification link.
Only verified users are allowed to log in and access their account.

**How It Works

1.User Registers**
User submits the registration form via /account/register/.

<img width="577" height="505" alt="Screenshot 2025-07-10 142519" src="https://github.com/user-attachments/assets/4d6d357d-8ae2-4c72-acd0-11599f2fac2a" />


**2.Verification Email Sent**
A unique verification link is sent to the user’s email using Django's send_mail() function and default_token_generator.

**3. User Verifies Account**
When the user clicks the link, their account is marked as verified.

**4. Login Enabled**
Only verified users can log in through /account/login/ and new memebers are redirected to create an account.
  
  **Files Involved**    
**views.py**
Handles registration, email sending, and token validation.

**urls.py**
Maps verification URLs like verify/<uidb64>/<token>/.

**register.html**
Registration form.

**email_verification.html**
Template used for sending email content (if HTML email is used).


**STEP 4: PROFILE MANAGEMENT **

**HOME PAGE**
This page welcomes you to our site and shows what our site can offer


<img width="1015" height="618" alt="Screenshot 2025-07-11 143143" src="https://github.com/user-attachments/assets/f44e1a5c-732f-43e1-8d1a-d68416ce77a3" />


This page would look like this:


<img width="955" height="440" alt="Screenshot 2025-07-11 150800" src="https://github.com/user-attachments/assets/49c5efb0-0cb0-40d0-bfbb-e50cb4e33b49" />



**REGISTRATION "Register"**
this page allows a new user to sign in and become part of our membership.


<img width="780" height="536" alt="Screenshot 2025-07-11 150325" src="https://github.com/user-attachments/assets/e7f7548c-2249-41af-8efa-ee6901a7229c" />



**LOGIN**

This page allows for a registered user to login to the site.

<img width="763" height="498" alt="Screenshot 2025-07-11 150133" src="https://github.com/user-attachments/assets/a90d17fb-e8fb-4ad3-b62e-202ac6f7d173" />



**PROFILE**

This page shows the 👤 user's details after registration and also after editing their profile.

<img width="946" height="507" alt="Screenshot 2025-07-11 150023" src="https://github.com/user-attachments/assets/14f208da-ca26-4e5f-8aa8-3c1a4b7ccb96" />


**Edit Profile**
Logged-in users can view their personal profile page.
Users can update their information (e.g., username, email, etc.).
Form is prefilled with current data for easy editing.
Upon successful update, a confirmation message is displayed.


<img width="1009" height="621" alt="Screenshot 2025-07-11 142403" src="https://github.com/user-attachments/assets/9d38e71d-fb23-46aa-b24c-99e70404248d" />

This page would look like this:


<img width="472" height="395" alt="Screenshot 2025-07-11 150927" src="https://github.com/user-attachments/assets/ddd59ac2-187f-4157-9ece-858d19b35391" />



**CHANGE PASSWORD**
This page allows a registered 👤 user or 👥 users to change oassword if they feel that they are 📒 not secured with the current password.


<img width="953" height="537" alt="Screenshot 2025-07-11 145937" src="https://github.com/user-attachments/assets/8d569871-141e-40e3-867b-a3f40366ec29" />

  The outcome should look like:


  <img width="450" height="260" alt="Screenshot 2025-07-11 151037" src="https://github.com/user-attachments/assets/1b9975a1-f625-458b-8c34-927df9bbeb10" />

  






