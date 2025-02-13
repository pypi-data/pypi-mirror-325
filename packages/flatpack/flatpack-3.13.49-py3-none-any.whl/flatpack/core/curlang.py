import shlex

from lark import Lark, Transformer

curlang_grammar = r"""
start: statement+
statement: cmd_stmt | delete_stmt | fail_stmt | find_stmt | get_stmt | make_stmt | pass_stmt | print_stmt

cmd_block: "{" cmd_content? "}"
cmd_content: /[^}]+/
cmd_stmt: "cmd" (cmd_block | RAW) ";"?

delete_stmt: "delete" STRING ";"?
fail_stmt: "fail" STRING
find_stmt: FIND_KEYWORD STRING block "else" STRING ";"?
get_stmt: "get" STRING "as" STRING (block)?
make_stmt: "make" STRING ";"?
pass_stmt: "pass" STRING
print_stmt: "print" STRING

block: "{" statement+ "}"
FIND_KEYWORD: "!find" | "find"

COMMENT: /#[^\n]*/
RAW: /[^\n]+/
STRING: /"([^"\\]*(\\.[^"\\]*)*)"/

%import common.WS
%ignore WS
%ignore COMMENT
"""


class CurlangTransformer(Transformer):
    def block(self, items):
        return items

    def cmd_block(self, items):
        return items[0] if items else ""

    def cmd_content(self, items):
        return items[0].value if hasattr(items[0], "value") else items[0]

    def cmd_stmt(self, items):
        return {"type": "cmd", "command": items[0].strip()}

    def delete_stmt(self, items):
        return {"type": "delete", "target": items[0]}

    def fail_stmt(self, items):
        return {"type": "fail", "message": items[0]}

    def find_stmt(self, items):
        return {
            "type": "find",
            "negated": (items[0] == "!find"),
            "filename": items[1],
            "block": items[2],
            "message": items[3]
        }

    def get_stmt(self, items):
        r = {"type": "get", "url": items[0], "destination": items[1]}

        if len(items) > 2:
            r["block"] = items[2]
        return r

    def make_stmt(self, items):
        return {"type": "make", "target": items[0]}

    def pass_stmt(self, items):
        return {"type": "pass", "message": items[0]}

    def print_stmt(self, items):
        return {"type": "print", "message": items[0]}

    def start(self, items):
        return items

    def statement(self, items):
        return items[0] if len(items) == 1 else items

    def RAW(self, token):
        return token.value

    def STRING(self, token):
        return token.value[1:-1]


parser = Lark(curlang_grammar, parser="lalr", transformer=CurlangTransformer())


def command_to_script(cmd):
    t = cmd.get("type")

    if t == "find":
        f = shlex.quote(cmd["filename"])
        m = shlex.quote(cmd["message"])
        c = ""

        if cmd.get("block"):
            c = "\n".join(command_to_script(x) for x in cmd["block"])

        if cmd["negated"]:
            return (
                f'if [ ! -f {f} ]; then\n'
                f'{c}\n'
                f'else\n'
                f'    echo {m}\n'
                f'fi'
            )
        else:
            return (
                f'if [ -f {f} ]; then\n'
                f'{c}\n'
                f'else\n'
                f'    echo {m}\n'
                f'fi'
            )
    elif t == "get":
        u = shlex.quote(cmd["url"])
        d = shlex.quote(cmd["destination"])
        dl = shlex.quote(
            f'Downloading from {cmd["url"]} to {cmd["destination"]}'
        )

        if cmd.get("block"):
            s, f_ = process_get_inner_block(cmd["block"])
            return (
                f'echo {dl}\n'
                f'curl -L {u} -o {d}\n'
                f'ret=$?\n'
                f'if [ $ret -eq 0 ]; then\n'
                f'    {s}\n'
                f'else\n'
                f'    {f_}\n'
                f'fi'
            )
        else:
            return f'echo {dl}\ncurl -L {u} -o {d}'
    elif t == "cmd":
        return cmd["command"]
    elif t == "delete":
        target = shlex.quote(cmd["target"])
        return f'rm -rf {target}'
    elif t == "make":
        target = shlex.quote(cmd["target"])
        return f'mkdir -p {target}'
    elif t == "pass":
        m = shlex.quote(f'PASS: {cmd["message"]}')
        return f'echo {m}'
    elif t == "fail":
        m = shlex.quote(f'FAIL: {cmd["message"]}')
        return f'echo {m}'
    elif t == "print":
        m = shlex.quote(cmd["message"])
        return f'echo {m}'
    else:
        u = shlex.quote(f'Unknown command type: {cmd}')
        return f'echo {u}'


def process_get_inner_block(block):
    success_cmds = []
    failure_cmds = []

    for cmd in block:
        if not isinstance(cmd, dict):
            raise ValueError(f"Expected dict in get inner block, got: {cmd}")

        if cmd["type"] == "pass":
            msg = shlex.quote(f'PASS: {cmd["message"]}')
            success_cmds.append(f'echo {msg}')
        elif cmd["type"] == "fail":
            msg = shlex.quote(f'FAIL: {cmd["message"]}')
            failure_cmds.append(f'echo {msg}')
        elif cmd["type"] == "print":
            msg = shlex.quote(cmd["message"])
            success_cmds.append(f'echo {msg}')
        else:
            unknown = shlex.quote(f'Unknown command type in get block: {cmd}')
            success_cmds.append(f'echo {unknown}')
            failure_cmds.append(f'echo {unknown}')
    return ("\n".join(success_cmds), "\n".join(failure_cmds))


def run_curlang_block(code):
    try:
        ast = parser.parse(code)
    except Exception as e:
        raise ValueError(f"Parsing error: {e}")

    r = []

    for cmd in ast:
        if not isinstance(cmd, dict):
            raise ValueError(f"Expected a dict, but got: {cmd}")

        r.append(command_to_script(cmd))
    return "\n".join(r)
