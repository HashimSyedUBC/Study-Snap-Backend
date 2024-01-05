
class Notes:
    def __init__(self, notes_name, course_id, user, final, note_id):
        # Initialize Course attributes
        self._notes_name = notes_name
        self._course_id = course_id
        self._test = final # List of tests
        self._user = user
        self._note_id = note_id
        

    # Getter and Setter for course_name
    @property
    def notes_name(self):
        """Getter for course_name."""
        return self._notes_name

    @notes_name.setter
    def notes_names(self, value):
        """Setter for notes_name."""
        self._notes_name = value

    # Getter and Setter for user
    @property
    def user(self):
        """Getter for uploader_id."""
        return self._user

    @user.setter
    def user(self, value):
        """Setter for uploader_id."""
        self._user = value

    # Getter and Setter for test
    @property
    def test(self):
        """Getter for test."""
        return self._test

    # Method to add a test
    def update_test(self, test):
        self._test = test
    
    def store_to_db():
        pass