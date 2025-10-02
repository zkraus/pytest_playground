from sut import sut_bug


class Sut:

    def __init__(self, auth_enable:bool=False):
        self.auth_enable = auth_enable
        self.users = ['admin']
        self._bug_mode = sut_bug.SUT_BUG

    def add_user(self, user:str):
        self.users.append(user)

    def enable_authorization(self):
        self.auth_enable = True

    def disable_authorization(self):
        self.auth_enable = False

    def get(self, user:str|None=None) -> tuple[int, str]:
        if self._bug_mode and self.auth_enable and user is None:
            return 500, "Server Error"
        if self.auth_enable:
            if not user in self.users:
                return 401, "Error: Unauthorized"
        else:
            if user:
                return 400, "Error: Bad Request"


        return 200, "Data!"
