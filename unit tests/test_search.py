"""
After running identification, the search should be saved.
"""
def search_storage_database():
    """
    If the user inputs and submits a search, the search should be stored in the
    backend database upon a successful request.
    """
    pass

def search_storage_display():
    """
    If the user inputs and submits a search, when they re-focus on the search
    input again, their previous search input should be displayed.
    """
    pass

def search_incomplete_not_stored():
    """
    If the user inputs a search but doesn’t submit it, the search should not be
    stored in the database or displayed as a “previous search” in the UI.
    """
    pass

"""
After successfully saving a search, loading the same search again should run the
model again.
"""
def same_database_same_input():
    """
    If the database didn’t change at all, the output should be the same as the 
    previous time the search was inputted.
    """
    pass

def single_model_output():
    """
    The model should generate exactly 1 output, given any input.
    """
    pass

"""
After failing to process/save a search, the search history/saved search list
should remain unchanged.
"""
def search_failure():
    """
    If the user inputs and submits a search, but the API request fails to update
    the backend database, the search should not be stored in the database or
    displayed as a “previous search” in the UI and an error message should be
    shown to the user.
    """
    pass
