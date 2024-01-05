import Course

class User:
    def __init__(self, name, user_id, university, courses=None):
        self.name = name
        self.user_id = user_id
        self.university = university
        self.courses = courses if courses else []

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        self._name = value

    # Getter for user_id
    @property
    def user_id(self):
        return self._user_id

    # Getter for university
    @property
    def university(self):
        return self._university

    # Setter for university
    @university.setter
    def university(self, value):
        self._university = value

    # Getter for courses
    @property
    def courses(self):
        return self._courses

    # Setter for courses
    @courses.setter
    def courses(self, value):
        if all(isinstance(course, Course) for course in value):
            self._courses = value
        else:
            raise ValueError("All items in the courses list must be Course objects")
