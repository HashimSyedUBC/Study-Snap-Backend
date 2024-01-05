
class Notes:
    def __init__(self, notes_name, course, user):
        # Initialize Course attributes
        self._notes_name = notes_name
        self._course = course
        self._sections = []  # List to hold Section objects
        self._test = [] # List of tests
        self._user = user
        

    # Getter and Setter for course_name
    @property
    def notes_name(self):
        """Getter for course_name."""
        return self._notes_name

    @notes_name.setter
    def course_name(self, value):
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

    # Getter and Setter for sections
    @property
    def sections(self):
        """Getter for sections."""
        return self._sections

    @sections.setter
    def sections(self, value):
        """Setter for sections."""
        if isinstance(value, list):
            self._sections = value
        else:
            raise ValueError("Sections should be a list")

    # Method to add a section
    def add_section(self, section):
        self._sections.append(section)

    # Getter and Setter for test
    @property
    def test(self):
        """Getter for test."""
        return self._test

    # Method to add a test
    def add_test(self, test):
        self._test.append(test)
    
    def store_to_db():
        pass