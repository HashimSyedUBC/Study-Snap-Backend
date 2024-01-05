class Sections:
    def __init__(self, section_name, summary, test, raw, note_id):
        # Initialize Sections attributes
        self._section_name = section_name
        self._summary = summary
        self._test = test
        self._order = 0
        self._raw_content = raw
        self._note_id = note_id

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
    
    def store_to_db():
        pass