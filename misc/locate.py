from talon import Module, actions, ui, ctrl
from talon.experimental.locate import locate
import time

mod = Module()


@mod.action_class
class Actions:
    def locate_hover(name: str, position: str = "") -> tuple[bool, int, int]:
        """Locate image and hover"""
        path = f"{actions.path.talon_user()}/andreas/images/{name}"
        rect = ui.active_window().rect
        t1 = time.perf_counter()
        locations = locate(path, rect=rect)

        if locations:
            print(f"located {name}: {time.perf_counter() - t1:0.3}s")
        else:
            print(f"Couldn't locate: {name}")
            return False, 0, 0

        location = locations[0]
        # Default to center
        x = location.x + location.width / 2
        y = location.y + location.height / 2
        if position == "left":
            x = location.left
        elif position == "top":
            y = location.top
        elif position == "right":
            x = location.right
        elif position == "bottom":
            y = location.bot

        ctrl.mouse_move(x, y)
        return True, x, y

    def locate_click(name: str, position: str = "") -> tuple[bool, int, int]:
        """Locate image and mouse left click"""
        ok, x, y = actions.user.locate_hover(name, position)
        if ok:
            ctrl.mouse_click(button=0)
        return ok, x, y

    def locate_drag(name: str, position: str = "") -> tuple[bool, int, int]:
        """Locate image and mouse left click drag"""
        ok, x, y = actions.user.locate_hover(name, position)
        if ok:
            ctrl.mouse_click(button=0, down=True)
        return ok, x, y
