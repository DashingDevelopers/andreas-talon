from talon import Module, Context, actions

mod = Module()
ctx = Context()

mod.tag("c_common")

ctx.matches = r"""
tag: user.c_common
tag: user.c_common
and tag: user.html # Solve conflict when using react typescript
"""


@ctx.action_class("user")
class UserActions:
    # Assignment operator
    def op_assign():
        actions.insert(" = ")

    # Math operators
    def op_sub():
        actions.insert(" - ")

    def op_sub_assign():
        actions.insert(" -= ")

    def op_add():
        actions.insert(" + ")

    def op_add_assign():
        actions.insert(" += ")

    def op_mult():
        actions.insert(" * ")

    def op_mult_assign():
        actions.insert(" *= ")

    def op_div():
        actions.insert(" / ")

    def op_div_assign():
        actions.insert(" /= ")

    def op_mod():
        actions.insert(" % ")

    def op_mod_assign():
        actions.insert(" %= ")

    # Comparison operators
    def op_less():
        actions.insert(" < ")

    def op_greater():
        actions.insert(" > ")

    def op_less_or_eq():
        actions.insert(" <= ")

    def op_greater_or_eq():
        actions.insert(" >= ")

    def op_not():
        actions.insert("!")

    def op_equal_null():
        actions.insert(" == null")

    def op_not_equal_null():
        actions.insert(" != null")

    # Comparison operators
    def op_equal():
        actions.insert(" == ")

    def op_not_equal():
        actions.insert(" != ")

    # Logical operators
    def op_and():
        actions.insert(" && ")

    def op_or():
        actions.insert(" || ")

    # Comments
    def comments_insert(text: str = ""):
        actions.insert(f"// {text}")

    def comments_insert_block(text: str = ""):
        actions.user.insert_snippet(f"/* {text}$0 */")

    def comments_insert_docstring(text: str = ""):
        actions.user.insert_snippet(f"/** {text}$0 */")

    # Miscellaneous statements
    def code_break():
        actions.insert("break;")

    def code_true():
        actions.insert("true")

    def code_false():
        actions.insert("false")

    def code_continue():
        actions.insert("continue;")

    def code_return():
        actions.insert("return ")

    # Function call
    def code_call_function(name: str):
        insert_snippet("functionCall", {"name": name})

    # Formatting getters
    def code_get_class_format() -> str:
        return "PASCAL_CASE"

    def code_get_function_format() -> str:
        return "CAMEL_CASE"

    def code_get_variable_format() -> str:
        return "CAMEL_CASE"


def insert_snippet(name: str, substitutions: dict[str, str] = None):
    actions.user.insert_snippet_by_name(
        f"c.{name}",
        substitutions,
    )
