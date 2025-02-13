#!/usr/bin/env python3
"""\
@file   popup.py
@author Nat Goodspeed
@date   2021-08-22
@brief  Command-line access to Python's tkinter.messagebox.

This module doesn't add much value for a Python consumer, which can itself
import and call tkinter.messagebox functions. Its purpose is to allow (e.g.) a
bash script to pop up a message box of interest. That being the case, we make
no provision for Python 2 compatibility.
"""

import importlib
from pyng.tk import get_root, tk
import sys

class Error(Exception):
    pass

def popup(function, title, message, **kwds):
    # Start by trying to import the relevant module. Split module.func; if
    # it's just func, prepend messagebox.
    submodname, funcname = (['messagebox'] + function.split('.'))[-2:]
    modname = 'tkinter.' + submodname
    try:
        module = importlib.import_module(modname)
    except ImportError as err:
        raise Error("Can't import '{}': {}".format(modname, err))

    try:
        func = getattr(module, funcname)
    except AttributeError as err:
        raise Error("Can't find {}.{}: {}".format(modname, funcname, err))

    # hide the dummy Tk window
    root = get_root()
    timeout = kwds.pop('timeout', None)
    if timeout:
        # https://stackoverflow.com/a/51651826
        root.after(timeout * 1000, root.destroy)

    try:
        return func(title, message, **kwds)
    except tk.TclError:
        # If in fact the timeout fires, destroying the main Tk instance before
        # the popup can query its own result raises TclError.
        return None

def main(*raw_args):
    from pyng.args import ParagraphArgumentParser
    parser = ParagraphArgumentParser(description="""
Display a specified Python popup with specified arguments.
""",
                            epilog=r"""
Different tkinter functions return different types. askfloat(), askinteger()
and askstring() return the type requested, which we print and terminate with 0.

If the user clicks Cancel, most functions return None. We distinguish None by
empty output and rc 3. (A valid empty input string from askstring produces rc
0.)

Some functions return bool (or None). Unless you specify --yesno, these
produce no output, but terminate with rc 0 (True) or 2 (False). We avoid rc 1
so the invoking script can distinguish an uncaught Python exception.

As of August 2021, valid function names include:\n
simpledialog.askfloat     # float, None\n
simpledialog.askinteger   # int, None\n
simpledialog.askstring    # str, None\n
showinfo                  # 'ok' (even for esc)\n
showwarning               # 'ok' (even for esc)\n
showerror                 # 'ok' (even for esc)\n
askquestion               # 'yes', 'no' (esc gives 'no') \n
askokcancel               # True, False\n
askretrycancel            # True, False\n
askyesno                  # True, False\n
askyesnocancel            # True, False, None

So without --yesno, the various user responses to askyesnocancel are
distinguished solely by rc 0 (Yes), 2 (No) or 3 (Cancel).
""")
    parser.add_argument(
        '-y', '--yesno', action='store_true', default=False,
        help="""for functions returning bool, emit 'y' or 'n' as well as
        setting the process return code""")
    parser.add_argument(
        '-t', '--timeout', type=int,
        help="""cancel the popup after TIMEOUT seconds""")
    parser.add_argument(
        'function',
        help="""[messagebox.]function: dynamically reference one of the
        convenience functions in tkinter.messagebox, or (if specified as
        module.function) another tkinter.module.function""")
    parser.add_argument(
        'title',
        help="""title for message box""")
    parser.add_argument(
        'message',
        help="""message for message box""")
    parser.add_argument(
        'keywords',
        nargs='*', default=[], metavar='KEYWORD=VALUE',
        help="""additional keyword arguments for specified function""")
    args = parser.parse_args(raw_args)

    popargs = args.__dict__.copy()
    yesno = popargs.pop('yesno')
    keywords = popargs.pop('keywords')
    kwds = dict(pair.split('=', 1) for pair in keywords)
    kwds.update(popargs)
    result = popup(**kwds)

    # What happens next depends on the type of the result. Any of these
    # functions can return None if the user clicks Cancel -- but it's hard to
    # specify an unambiguous way to convey None to the invoker of this script.
    # Empty string or 'None' or whatever might actually be valid input
    # strings. Let's try saying nothing with rc 3 (rc 1 being used by Python
    # itself for uncaught exceptions).
    if result is None:
        return 3

    # Several of these functions return True or False. Catch those first
    # because isinstance(True, int) is True! Fortunately isinstance(1, bool)
    # is not.
    if isinstance(result, bool):
        if yesno:
            print({True: 'y', False: 'n'}[result])
        # convert True result to bash true, False to (what bash will accept
        # as) false. Use 2 since Python returns 1 for uncaught exceptions.
        return 0 if result else 2

    # Anything else (float, int or string are the possibilities we know
    # about), print it and exit with rc 0.
    print(result)
    return 0

# special entry point for script generated by setup.py
def script():
    try:
        sys.exit(main(*sys.argv[1:]))
    except Error as err:
        sys.exit(str(err))

if __name__ == "__main__":
    script()
