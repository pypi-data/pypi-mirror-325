from lark import Lark, Transformer

curlang_grammar = r"""
    start: statement+
    statement: find_stmt | get_stmt | pass_stmt | fail_stmt
    find_stmt: "!find" STRING block "else" STRING ";"? 
    block: "{" statement+ "}"
    get_stmt: "get" STRING "as" STRING (block)?
    pass_stmt: "pass" STRING
    fail_stmt: "fail" STRING
    STRING: /"([^"\\]*(\\.[^"\\]*)*)"/
    COMMENT: /#[^\n]*/
    %import common.WS
    %ignore WS
    %ignore COMMENT
"""


class CurlangTransformer(Transformer):
    def start(self, items):
        return items

    def statement(self, items):
        return items[0] if len(items) == 1 else items

    def block(self, items):
        return items

    def find_stmt(self, items):
        return {"type": "find", "filename": items[0], "block": items[1],
                "message": items[2]}

    def get_stmt(self, items):
        result = {"type": "get", "url": items[0], "destination": items[1]}
        if len(items) > 2:
            result["block"] = items[2]
        return result

    def pass_stmt(self, items):
        return {"type": "pass", "message": items[0]}

    def fail_stmt(self, items):
        return {"type": "fail", "message": items[0]}

    def STRING(self, token):
        return token.value[1:-1]


parser = Lark(curlang_grammar, parser='lalr', transformer=CurlangTransformer())


def process_get_inner_block(block) -> (str, str):
    """
    Process the inner block for a get statement.
    Returns a tuple (success_commands, failure_commands).
    """
    success_cmds = []
    failure_cmds = []

    for cmd in block:
        if not isinstance(cmd, dict):
            raise ValueError(f"Expected dict in get inner block, got: {cmd}")

        if cmd["type"] == "pass":
            success_cmds.append(f'echo "SUCCESS: {cmd["message"]}"')
        elif cmd["type"] == "fail":
            failure_cmds.append(f'echo "FAILURE: {cmd["message"]}"')
        else:
            success_cmds.append(
                f'echo "Unknown command type in get block: {cmd}"'
            )
            failure_cmds.append(
                f'echo "Unknown command type in get block: {cmd}"'
            )
    return ("\n".join(success_cmds), "\n".join(failure_cmds))


def run_curlang_block_inner(cmd) -> str:
    """
    Recursively process a single command dictionary from an inner block.
    """
    if cmd["type"] == "find":
        filename = cmd["filename"]
        message = cmd["message"]
        inner_code = ""

        if "block" in cmd and cmd["block"]:
            inner_commands = [
                run_curlang_block_inner(inner) for inner in
                cmd["block"]
            ]

            inner_code = "\n".join(inner_commands)
        return (
            f'if [ ! -f "{filename}" ]; then\n'
            f'    echo "File {filename} not found. Executing block..."\n'
            f'{inner_code}\n'
            f'else\n'
            f'    echo "{message}"\n'
            f'fi'
        )
    elif cmd["type"] == "get":
        url = cmd["url"]
        destination = cmd["destination"]
        if "block" in cmd and cmd["block"]:
            success_code, failure_code = process_get_inner_block(cmd["block"])
            return (
                f'echo "Downloading from {url} to {destination}"\n'
                f'curl -L "{url}" -o "{destination}"\n'
                f'ret=$?\n'
                f'if [ $ret -eq 0 ]; then\n'
                f'    {success_code}\n'
                f'else\n'
                f'    {failure_code}\n'
                f'fi'
            )
        else:
            return (
                f'echo "Downloading from {url} to {destination}"\n'
                f'curl -L "{url}" -o "{destination}"'
            )
    elif cmd["type"] == "pass":
        return f'echo "SUCCESS: {cmd["message"]}"'
    elif cmd["type"] == "fail":
        return f'echo "FAILURE: {cmd["message"]}"'
    else:
        return f'echo "Unknown command type: {cmd}"'


def run_curlang_block(code: str) -> str:
    """
    Parse the curlang code, generate an AST, and convert it into
    Bash commands that perform the desired actions.
    Returns a string that can be inserted into a Bash script.
    """
    try:
        ast = parser.parse(code)
    except Exception as e:
        raise ValueError(f"Parsing error: {e}")

    commands = []

    for cmd in ast:
        if not isinstance(cmd, dict):
            raise ValueError(f"Expected a dict, but got: {cmd}")

        if cmd["type"] == "find":
            filename = cmd["filename"]
            message = cmd["message"]
            inner_code = ""

            if "block" in cmd and cmd["block"]:
                inner_commands = [
                    run_curlang_block_inner(inner) for inner in
                    cmd["block"]
                ]

                inner_code = "\n".join(inner_commands)

            commands.append(
                f'if [ ! -f "{filename}" ]; then\n'
                f'    echo "File {filename} not found. Executing block..."\n'
                f'{inner_code}\n'
                f'else\n'
                f'    echo "{message}"\n'
                f'fi'
            )
        elif cmd["type"] == "get":
            url = cmd["url"]
            destination = cmd["destination"]

            if "block" in cmd and cmd["block"]:
                success_code, failure_code = process_get_inner_block(
                    cmd["block"]
                )

                commands.append(
                    f'echo "Downloading from {url} to {destination}"\n'
                    f'curl -L "{url}" -o "{destination}"\n'
                    f'ret=$?\n'
                    f'if [ $ret -eq 0 ]; then\n'
                    f'    {success_code}\n'
                    f'else\n'
                    f'    {failure_code}\n'
                    f'fi'
                )
            else:
                commands.append(
                    f'echo "Downloading from {url} to {destination}"\n'
                    f'curl -L "{url}" -o "{destination}"'
                )
        elif cmd["type"] == "pass":
            commands.append(f'echo "SUCCESS: {cmd["message"]}"')
        elif cmd["type"] == "fail":
            commands.append(f'echo "FAILURE: {cmd["message"]}"')
        else:
            commands.append(f'echo "Unknown command type: {cmd}"')
    return "\n".join(commands)
