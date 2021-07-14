from talon import Context, Module, actions
import os

key = actions.key
mod = Module()


@mod.action_class
class Actions:
    def exec(command: str):
        """Run command"""
        os.system(command)

    def shut_down_os():
        """Shut down operating system"""


# ----- Windows -----


ctx_win = Context()

ctx_win.matches = r"""
os: windows
"""


@ctx_win.action_class("user")
class UserActionsWin:
    def exec(command: str):
        key("super-r")
        actions.sleep("30ms")
        actions.insert(command)
        key("enter")

    def shut_down_os():
        key("super-x u")
