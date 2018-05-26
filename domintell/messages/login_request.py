"""
:author: Zilvinas Binisevicius <zilvinas@binis.me>
"""
import domintell


class LoginRequest(domintell.Command):
    """
        send: LOGIN<password_hash>
    """
    def __init__(self, password_hash):
        domintell.Command.__init__(self, "_LOGIN_", "_LOGIN_")
        self._password = password_hash

    def command(self):
        # TODO FIXME
        # return "LOGIN" + self._password
        return self._password

    def is_binary(self):
        return True

