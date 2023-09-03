from talon import Module, Context, actions
from ..tags.operators import CodeOperators

mod = Module()
ctx = Context()

ctx.matches = r"""
code.language: python
"""

# fmt: off
ctx.lists["self.code_operator"] = CodeOperators(
    op_assign        = " = ",
    op_sub           = " - ",
    op_sub_assign    = " -= ",
    op_add           = " + ",
    op_add_assign    = " += ",
    op_mult          = " * ",
    op_mult_assign   = " *= ",
    op_div           = " / ",
    op_div_assign    = " /= ",
    op_mod           = " % ",
    op_mod_assign    = " %= ",
    op_pow           = " ** ",
    is_equal         = " == ",
    is_not_equal     = " != ",
    is_less          = " < ",
    is_greater       = " > ",
    is_less_equal    = " <= ",
    is_greater_equal = " >= ",   
    is_not           = "not ",
    is_null          = " is None",
    is_not_null      = " is not None",
    is_in            = " in ",
    op_and           = " and ",
    op_or            = " or ",
)
access_modifiers = {
    "public": "",
    "protected": "_",
    "private": "__",
}
ctx.lists["self.code_class_modifier"] = {}
ctx.lists["self.code_function_modifier"] = access_modifiers
ctx.lists["self.code_variable_modifier"] = {
    **access_modifiers,
    "global": "global",
}
ctx.lists["self.code_data_type"] = {
    "string"   : "str",
    "int"      : "int",
    "float"    : "float",
    "complex"  : "complex",
    "bool"     : "bool",
    "dict"     : "dict",
    "set"      : "set",
    "list"     : "list",
    "range"    : "range",
    "none"     : "None",
    "any"      : "Any",
    "tuple"    : "tuple",
    "union"    : "Union",
    "optional" : "Optional",
}
ctx.lists["self.code_call_function"] = {
    "format",
    "strip",
    "lstrip",
    "rstrip",
    "replace",
    "split",
    "len",
    "type",
    "range",
    "find",
    "join",
    "sorted",
    "filter",
    "dir",
    "isinstance",
    "enumerate",
}
ctx.lists["self.code_insert"] = {
    "true"      : "True",
    "false"     : "False",
    "None"      : "None",
    "self"      : "self",
    "pass"      : "pass",
    "from"      : "from ",
    "regex"     : "re",
    "return"    : "return ",
    "import"    : "import ",
    "def"       : "def ",
    "class"     : "class ",
    "lambda"    : "lambda: ",
    "global"    : "global ",
    "raise"     : "raise ",
    "yield"     : "yield ",
    "break"     : "break",
    "exception" : "Exception",
    "continue"  : "continue",
}
# fmt: on


@ctx.action_class("user")
class UserActions:
    # Miscellaneous statements
    def insert_arrow():
        actions.insert(" -> ")

    # Class statement
    def code_class(name: str, modifiers: list[str]):
        actions.user.code_insert_snippet("classDeclaration", {"name": name})

    # Constructor statement
    def code_constructor(modifiers: list[str]):
        actions.user.code_insert_snippet("constructorDeclaration")

    # Function statement
    def code_function(name: str, modifiers: list[str]):
        actions.user.code_insert_snippet(
            "functionDeclaration",
            {"name": f"{''.join(modifiers)}{name}"},
        )

    # Variable statement
    def code_variable(
        name: str, modifiers: list[str], assign: bool, data_type: str = None
    ):
        text = name
        if modifiers:
            text = f"{' '.join(modifiers)} {text}"
        if data_type:
            text = f"{text}: {data_type}"
        if assign:
            text += " = "
        actions.insert(text)

    # Insert types
    def code_insert_type_annotation(type: str):
        actions.insert(f": {type}")

    def code_insert_return_type(type: str):
        actions.insert(f" -> {type}")

    # Formatting getters
    def code_get_class_format() -> str:
        return "PASCAL_CASE"

    def code_get_function_format() -> str:
        return "SNAKE_CASE"

    def code_get_variable_format() -> str:
        return "SNAKE_CASE"
