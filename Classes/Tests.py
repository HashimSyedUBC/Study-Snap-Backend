import Questions

class Test:
    def __init__(self, test_id, section_id):
        self.test_id = test_id
        self.section_id = section_id

    # Getter for test_id
    @property
    def test_id(self):
        return self.test_id

    # Getter for section_ids
    @property
    def section_ids(self):
        return self.section_id

