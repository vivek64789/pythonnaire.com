"""class StartApp"""
"""class ConnectDatabase"""
"""class DatabaseConnected"""


"""class LoginForm in login_form module allows user to login to the system by providing them user interface, it verifies
username/email and password from the unverified and admin table of database, if user exists it check for password
and allow them to login if it matched, otherwise popup error message. if user exists but has not verified their
email, it will ask them to verify their email address so that they can login, only after successful verification
of email they will be allowed to login to the system. it also allow user to login to the system by providing OTP
instead of password, it will first verify that username/email with existing data and if password left blank, will
ask them if they want to login in using OTP. if user want to login using OTP, an unique OTP will be sent to
the associated email address.
this module also inherits Inherits and extend the functionality of AdminDashboard class, by adding the feature of 
current active user.
also, inherits NonVerified class from non_verified module in order to verify the user email address
by Validating the OTP and shifts unverified credentials of user to
verified admin table of database after successful verification of"""


"""class NonVerified in non_verified module is user interface to verify OTP for those user who are not verified but have 
already created an account."""


"""class OtpVerification in otp_verification module sends OTP to email address that the user want to change the 
password after forgot password, this will 
send OTP and validates those OTP with user input, if matched another window will open allowing them to 
register new password, otherwise leave them error message displaying system can not verify the user.
also, inherits ForgotPassword class in order to let user change their password on user interface
it will fetch the email address of the user that they just validates by OTP and change the password
in database admin table"""


"""class ForgotPassword in forgot_password module Allows user to forgot password from GUI, Let user choose new password,
and update those password to the database searching from email address that the user
used in the verification process, after successful password changes, an email
notification about recent password changed is sent to email address of that user
with time and date when the password was changed."""


"""class AdminDashboard in admin_dashboard module comes in use when user successfully login to the system, 
it allows user to view brief information about students, employees and department in click_home() method, 
let user manage the system such as, students, employees, department, courses, section, batch from click_manage() 
method, also it allows user to view partial data about students, employees, departments and course from click_view() 
method. lastly, it also allows them to change their current password if they remember current password from 
click_setting() methods """

"""class ManageStudent in manage_student module Allows Admin to manage students; add, update, delete, fetch the data, 
here, admin can view all the details of students and have various option to perform, they can search the by different 
functionality, such as student_id, name, email, phone number and also they can search data such as id name and email 
from one date to another. searching can be performed even just by providing the character that the students detail 
may contain and it will fetch all the data regarding that. this was done by using wild card feature of MySQL after 
grabbing all the data and then performing bubble sort on that and later sent to binary search method if data exists 
then all the data were inserted on the student tree view. to make sorting possible, bubble sort method is used. also 
this method is used to sort the data in order to search. 
also, this class inherits RegisterForm class and overrides 
the functionality by configuring the submit button from performing add student to update students. this class get the 
list of data that is selected on student tree view and insert those data automatically into the respected fields, 
it do not allow the admin to update username of the user and restricts to change the password displaying error 
message as only user can change their password
moreover, it inherits RegisterForm and extend the functionality by fetching the data of selected student in order to let 
user add students by grabbing their data directly into the registration form which will save time of the admin
 """

"""class StudentRegistration in student_registration Module allows admin to register students, it validates, 
if that username and email address already exists or not, if it  exists then proper error message is thrown to let 
them know that these user already exists. all the validations of entry fields are done here for registration form so 
that in order to add students all fields are required. before able to add students, there are pre requisites need to 
be fulfilled, such as course, batch and section should already been added other wise error message showing those data 
should be added first are being displayed. to avoid the error if pre requisites is not fulfilled exception handling 
is done while setting current index of combobox.
another class in this module is Clock which creates an working 
clock using different module, and displayed those function onto a clock image which is static """

"* all other Manage and Register form are similar in functionality with ManageStudent class and RegisterForm class"
