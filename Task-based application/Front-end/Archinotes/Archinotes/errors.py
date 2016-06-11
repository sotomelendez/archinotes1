class LoginFailedError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def str(self):
        return repr(self.msg)

class UserTokenError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def str(self):
        return repr(self.msg)

class WsError(Exception):
	def __init__(self, msg):
		self.msg = msg

	def str(self):
		return repr(self.msg)