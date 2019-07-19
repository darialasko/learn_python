from user_class import User


class Moderator(User):
    total_mods = 0
    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.active_users} active moderators"

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.total_mods += 1

    def remove_post(self):
        return f"{self.full_name()} removed a post from the {self.community} community"


m = Moderator("Daria", "Lasko", 20, "PL")
print(m.remove_post())
