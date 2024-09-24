from core.Skill import Skill


class Student:
    _id = 0

    def __init__(self, registration, name, email, course, bio, skills):
        self.id: int = Student._id
        self.registration: str = registration
        self.name: str = name
        self.email: str = email
        self.course: str = course
        self.bio: str = bio
        self.skills: Skill = skills

        Student._id += 1
