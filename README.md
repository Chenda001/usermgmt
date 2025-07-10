
**STEP 1: PROJECT SET UP**
  I started by by setting up my project by by the name "user-mgmt" and create an app and named it 'accounts'. 
  I then added added it in the installed apps in the user-mgmt/setting.py ensure that django recognises the app.
  
  ![Screenshot 2025-07-07 150955](https://github.com/user-attachments/assets/54b7c5bf-05e5-4b22-8637-3cf51dee7f6a)


**STEP 2: User Registration.**

This project includes a simple user authentication system using Django's built-in tools.

it What’s Implemented
User Registration
Uses Django’s UserCreationForm
Allows users to register with a username, email, and password
Accessible at: /accounts/register/

![Screenshot 2025-07-07 193610](https://github.com/user-attachments/assets/ad09a7ec-8482-473f-8e91-181c3f70ec00)


_User Login_
Uses Django’s built-in LoginView
Allows registered users to log in securely
Accessible at: /accounts/login/

![Screenshot 2025-07-07 194754](https://github.com/user-attachments/assets/459444f6-3b42-49a0-91b2-c02ec12b51e6)



**Redirection**
Upon successful login, users are redirected to the home page (/)



**STEP 3: Email Verification (Custom Django Feature)
Description**

This project implements email verification as part of the user registration process. After a user registers, a confirmation email is sent with a verification link. Only verified users are allowed to log in and access their account.
**How It Works
1.User Registers**
User submits the registration form via /account/register/.
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
![Screenshot 2025-07-07 194733](https://github.com/user-attachments/assets/3db18174-ddfa-4202-b0b2-37f143fe871d)


![Screenshot 2025-07-07 200443](https://github.com/user-attachments/assets/40c2e487-31be-4d8a-ad67-8a8018c8e3b3)










=======
Planned Features

User Registration & Login
Email Verification
Profile View & Edit
Change Password
Admin Panel
Unit Tests (models and views)


1. Project set up

    I started by by setting up my project by by the name "user-mgmt" and create an app and named it accounts. To ensure that django recognises the app, i added it in the installed apps in the user-mgmt/setting.py.

    
>>>>>>> cdcaf01 (my commit)
