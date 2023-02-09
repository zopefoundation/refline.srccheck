# this is a !!MODIFIED!!! version of the original pyflakes script
# this one returns the warnings instead of printing them to stdout

"""
Implementation of the command-line I{pyflakes} tool.
"""

import _ast
import os
import sys


checker = __import__('pyflakes.checker').checker


def check(codeString, filename):
    """
    Check the Python source given by C{codeString} for flakes.

    @param codeString: The Python source to check.
    @type codeString: C{str}

    @param filename: The name of the file the source came from, used to report
        errors.
    @type filename: C{str}

    @return: List of warnings emitted.
    """
    # Since compiler.parse does not reliably report syntax errors, use the
    # built in compiler first to detect those.
    try:
        compile(codeString, filename, "exec")
    except (SyntaxError, IndentationError) as value:
        msg = value.args[0]

        (lineno, offset, text) = value.lineno, value.offset, value.text

        # If there's an encoding problem with the file, the text is None.
        if text is None:
            # Avoid using msg, since for the only known case, it contains a
            # bogus message that claims the encoding the file declared was
            # unknown.
            return "{}: problem decoding source".format(filename)
        else:
            line = text.splitlines()[-1]

            if offset is not None:
                offset = offset - (len(text) - len(line))

            result = '%s:%d: %s\n%s' % (filename, lineno, msg, line)

            if offset is not None:
                result += '\n'+" " * offset+"^"

        return result
    else:
        # Okay, it's syntactically valid.  Now parse it into an ast and check
        # it.
        tree = compile(codeString, filename, "exec", _ast.PyCF_ONLY_AST)
        w = checker.Checker(tree, filename)
        w.messages.sort(key=lambda x: x.lineno)
        return w.messages


def checkPath(filename):
    """
    Check the given path, printing out any warnings detected.

    @return: the number of warnings printed
    """
    try:
        return check(open(filename).read() + '\n', filename)
    except OSError as msg:
        print("{}: {}".format(filename, msg.args[1]), file=sys.stderr)
        return 1


def main():
    warnings = 0
    args = sys.argv[1:]
    if args:
        for arg in args:
            if os.path.isdir(arg):
                for dirpath, dirnames, filenames in os.walk(arg):
                    for filename in filenames:
                        if filename.endswith('.py'):
                            warnings += checkPath(
                                os.path.join(dirpath, filename))
            else:
                warnings += checkPath(arg)
    else:
        warnings += check(sys.stdin.read(), '<stdin>')

    raise SystemExit(warnings > 0)
