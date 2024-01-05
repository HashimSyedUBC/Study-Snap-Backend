class Course:
    def __init__(self, course_name, course_code, uploader_id, university):
        # Initialize Course attributes
        self._course_name = course_name
        self._course_code = course_code
        self._uploader_id = uploader_id
        self._university = university
        self._sections = []  # List to hold Section objects
        self._test = []

    # Getter and Setter for course_name
    @property
    def course_name(self):
        """Getter for course_name."""
        return self._course_name

    @course_name.setter
    def course_name(self, value):
        """Setter for course_name."""
        self._course_name = value

    # Getter and Setter for course_code
    @property
    def course_code(self):
        """Getter for course_code."""
        return self._course_code

    @course_code.setter
    def course_code(self, value):
        """Setter for course_code."""
        self._course_code = value

    # Getter and Setter for uploader_id
    @property
    def uploader_id(self):
        """Getter for uploader_id."""
        return self._uploader_id

    @uploader_id.setter
    def uploader_id(self, value):
        """Setter for uploader_id."""
        self._uploader_id = value

    # Getter and Setter for university
    @property
    def university(self):
        """Getter for university."""
        return self._university

    @university.setter
    def university(self, value):
        """Setter for university."""
        self._university = value

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

    @test.setter
    def test(self, value):
        """Setter for test."""
        if isinstance(value, list):
            self._test = value
        else:
            raise ValueError("Test should be a list")

    # Method to add a test
    def add_test(self, test):
        self._test.append(test)

class Sections:
    def __init__(self, section_name, summary, test, raw):
        # Initialize Sections attributes
        self._section_name = section_name
        self._summary = summary
        self._test = test
        self._order = 0
        self._raw_content = raw

    # Getter and Setter for section_name
    @property
    def section_name(self):
        """Getter for section_name."""
        return self._section_name

    @section_name.setter
    def section_name(self, value):
        """Setter for section_name."""
        self._section_name = value

    # Getter and Setter for summary
    @property
    def summary(self):
        """Getter for summary."""
        return self._summary

    @summary.setter
    def summary(self, value):
        """Setter for summary."""
        self._summary = value

    # Getter and Setter for test
    @property
    def test(self):
        """Getter for test."""
        return self._test

    @test.setter
    def test(self, value):
        """Setter for test."""
        self._test = value

    # Getter and Setter for order
    @property
    def order(self):
        """Getter for order."""
        return self._order

    @order.setter
    def order(self, value):
        """Setter for order."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Order must be a non-negative integer")
        self._order = value
