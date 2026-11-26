class Round:
    def __init__(self, title, task, hint, clue):
        self.title = title
        self.task = task
        self.hint = hint
        self.clue = clue

    def check(self, pattern):
        return False, ""
