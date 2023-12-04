"""
After updating a username, pfp & password should remain unchanged.
"""
def test_username_change_only():
    """
    After changing their username & ONLY their username, the username displayed 
    in the UI and stored in the database should change, but nothing else.
    """
    pass

def test_username_and_other_changes():
    """
    After changing their username and other pieces of data for their profile,
    the username displayed in the UI and stored in the database should change.
    """
    pass

"""
After successfully resetting a password, the user shouldn’t be able to log in
with the previous password.
"""
def old_password_fails():
    """
    Attempting to log in with the old password doesn’t provide access to the
    account.
    """
    pass

def new_password_succeeds():
    """
    Attempting to log in with the new password provides access to the 
    account.
    """
    pass

def incorrect_password_fails():
    """
    Attempting to log in with neither the old or new passwords doesn’t provide
    access to the account.
    """

