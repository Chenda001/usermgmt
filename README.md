
**STEP 1: PROJECT SET UP**

  I started by by setting up my project by by the name "user-mgmt" and create an app and named it 'accounts'. 
  I then added added it in the installed apps in the user-mgmt/setting.py ensure that django recognises the app.
  
<img width="276" height="114" alt="Screenshot 2025-07-07 150955" src="https://github.com/user-attachments/assets/1346d570-0da6-4c39-847f-ed22b4c6f238" />


**STEP 2: User Registration.**

This project includes a simple user authentication system using Django's built-in tools.

it What’s Implemented
User Registration
Uses Django’s UserCreationForm
Allows users to register with a username, email, and password
Accessible at: /accounts/register/

<img width="659" height="97" alt="Screenshot 2025-07-07 193610" src="https://github.com/user-attachments/assets/287e18ef-eb0a-420d-9570-842de9b70051" />


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

**Edit Profile**
Logged-in users can view their personal profile page.
Users can update their information (e.g., username, email, etc.).
Form is prefilled with current data for easy editing.
Upon successful update, a confirmation message is displayed.

<img width="773" height="255" alt="Screenshot 2025-07-07 194733" src="https://github.com/user-attachments/assets/dc463aa3-af52-4d61-b9c1-012368f8d48b" />



<img width="802" height="426" alt="Screenshot 2025-07-07 200443" src="https://github.com/user-attachments/assets/664ab7f6-d8b6-4f26-949c-7bfa83a1fce2" />






