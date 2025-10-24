import uuid

class UserFacade:
    def __init__(self):
        self.users = {}

    def get_users(self):
        return list(self.users.values())

    def create_user(self, email, first_name, last_name, password=None):
        # Check for duplicate email
        for user in self.users.values():
            if user['email'] == email:
                raise ValueError("Email already registered")

        user_id = str(uuid.uuid4())
        user = {
            "id": user_id,
            "email": email,
            "first_name": first_name,
            "last_name": last_name
        }
        self.users[user_id] = user
        return user

    def get_user(self, user_id):
        return self.users.get(user_id, None)

    def update_user(self, user_id, **kwargs):
        user = self.users.get(user_id)
        if not user:
            return None

        # Prevent duplicate email if changing it
        if "email" in kwargs and kwargs["email"] != user["email"]:
            for u in self.users.values():
                if u["email"] == kwargs["email"]:
                    raise ValueError("Email already registered")

        user.update({k: v for k, v in kwargs.items() if v is not None})
        return user
