class Course:
    def __init__(self, course_name, course_code, course_year, university) -> None:
        self._course_name = course_name
        self.course_year = course_year
        self._course_code = course_code
        self._university = university
        self.notes = []

    # Getter and Setter for course_name
    @property
    def course_name(self):
        """Getter for course_name."""
        return self._notes_name

    @course_name.setter
    def course_name(self, value):
        """Setter for notes_name."""
        self._notes_name = value
    
    # Getter and Setter for course_code
    @property
    def course_code(self):
        """Getter for course_code."""
        return self._course_code

    @course_code.setter
    def course_code(self, value):
        """Setter for course_code."""
        self._course_code = value

    @property
    def course_year(self):
        return self.course_year

    @course_year.setter
    def course_year(self, course_year):
        self.course_year = course_year

    # Getter and Setter for university
    @property
    def university(self):
        """Getter for university."""
        return self._university

    @university.setter
    def university(self, value):
        """Setter for university."""
        self._university = value
        
    # Method to add notes
    def add_notes(self, notes):
        self._sections.append(notes)
    
    def store_to_db():
        pass