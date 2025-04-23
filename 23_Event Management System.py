class Event:
    def __init__(self, name, date, location):
        self.name = name
        self.date = date
        self.location = location
        self.participants = []
        self.activities = []

    def register_participant(self, participant):
        self.participants.append(participant)
        print(f"{participant.name} registered for {self.name}.")

    def add_activity(self, activity):
        self.activities.append(activity)
        print(f"Activity '{activity.name}' added to {self.name}.")

    def event_details(self):
        print(f"Event: {self.name}\nDate: {self.date}\nLocation: {self.location}")
        print("Participants:", ", ".join([p.name for p in self.participants]))
        print("Activities:", ", ".join([a.name for a in self.activities]))

class Participant:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Activity:
    def __init__(self, name, time):
        self.name = name
        self.time = time


# Creating Event, Participants, and Activities
event1 = Event(" Hackathon & Robo Racing ", "2025-04-30", "Main Auditorium")
participant1 = Participant("Parth", "Parth@example.com")
participant2 = Participant("Aryan", "arayan02@example.com")
activity1 = Activity("Coding Competition", "11:00 AM")
activity2 = Activity("Robotics Workshop", "4:00 PM")

# Registering participants and adding activities
event1.register_participant(participant1)
event1.register_participant(participant2)
event1.add_activity(activity1)
event1.add_activity(activity2)

# Displaying event details
event1.event_details()
