from typing import Optional

class PasswordManager:

    def __init__(self, password: str):
        self._password = password
    
    def changePassword(self, emailAddress: Optional[str] = None, phoneNumber: Optional[int] = None, password: str = ""):

        if emailAddress is not None:
            self.email(emailAddress, password)
        elif phoneNumber is not None:
            self.phoneNumber(phoneNumber, password)
        else:
            raise ValueError("Must provide email or phone number")
    
    def email(self, emailAddress: str, newPassword: str):
        print(f"Passwowrd changed with email: {emailAddress}. New Password is {newPassword}")
        self._password = newPassword
    
    def phoneNumber(self, number: int, newPassword: str):
        print(f"Passwowrd changed with nummber: {number}. New Password is {newPassword}")
        self._password = newPassword


password = PasswordManager("SnoopyIsAmazing")
password.changePassword(emailAddress="JhonaTech@gmail.com", password="CharlieBrownIsBetter")
