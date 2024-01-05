class Question:
    def __init__(self, question_id, options, answer, test_id):
        self._question_id = question_id
        self._options = options
        self._answer = answer
        self.test_id = test_id

    # Getter for question_id
    @property
    def question_id(self):
        return self._question_id

    # Getter for options
    @property
    def options(self):
        return self._options

    # Setter for options
    @options.setter
    def options(self, value):
        self._options = value

    # Getter for answer
    @property
    def answer(self):
        return self._answer

    # Setter for answer
    @answer.setter
    def answer(self, value):
        if value in self._options:
            self._answer = value
        else:
            raise ValueError("Answer must be one of the options")
