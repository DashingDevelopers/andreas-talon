from talon import Module, actions

mod = Module()

mod.list("delimiter_pair", "List of matching pair delimiters")
mod.list(
    "delimiter_pair_wrap",
    "List of matching pair delimiters use specifically for wrapping",
)


@mod.capture(rule="{user.delimiter_pair}")
def delimiter_pair(m) -> list[str]:
    return parse_pair(m.delimiter_pair)


@mod.capture(rule="{user.delimiter_pair} | {user.delimiter_pair_wrap}")
def delimiter_pair_wrap(m) -> list[str]:
    return parse_pair(m[0])


def parse_pair(pair_str: str) -> list[str]:
    pair = pair_str.split()
    assert len(pair) == 2
    open = pair[0] if pair[0] != "space" else " "
    close = pair[1] if pair[1] != "space" else " "
    return [open, close]


@mod.action_class
class Actions:
    def delimiter_pair_insert(pair: list[str]):
        """Insert a delimiter pair <pair> leaving the cursor in the middle"""
        left, right = pair
        actions.insert(f"{left}{right}")
        for _ in right:
            actions.edit.left()

    def delimiter_pair_wrap_selection(pair: list[str]):
        """Wrap selection with delimiter pair <pair>"""
        left, right = pair
        selected = actions.edit.selected_text()
        actions.insert(f"{left}{selected}{right}")
        for _ in right:
            actions.edit.left()
