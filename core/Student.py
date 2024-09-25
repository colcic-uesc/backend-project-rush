class Student:
    _id = 0

    def __init__(self, registration, name, email, course, bio, skills):
        self.id: int = Student._id

        if not isinstance(registration, str):
            raise ValueError("registration must be a string")

        if not isinstance(name, str):
            raise ValueError("name must be a string")

        if not isinstance(email, str):
            raise ValueError("email must be a string")

        if not isinstance(course, str):
            raise ValueError("course must be a string")

        if not isinstance(bio, str):
            raise ValueError("bio must be a string")

        if not isinstance(skills, list):
            raise ValueError("skills must be a list of integers")

        for skill in skills:
            if not isinstance(skill, int):
                raise ValueError("skills must be a list of integers")

        self.registration: str = registration
        self.name: str = name
        self.email: str = email
        self.course: str = course
        self.bio: str = bio
        self.skills: list[int] = skills

        Student._id += 1
