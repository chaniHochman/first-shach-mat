class Command:
    def __init__(self, command_type, source=None, destination=None):
        self.command_type = command_type
        self.source = source
        self.destination = destination

    #הצגת הפקודה בצורה יפה
    def __str__(self):
        return f"{self.command_type}: {self.source} -> {self.destination}"