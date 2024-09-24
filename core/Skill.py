class Skill:
    _id = 0

    def __init__(self, name):
        self.id: int = Skill._id
        self.name: str = name

        Skill._id += 1
