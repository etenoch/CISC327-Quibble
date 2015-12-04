# CISC327 Quibble
#   Team Apus
#   Adam Perron (10106523)
#   Enoch Tam (10094398)

# Error Class

class QuibbleError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)