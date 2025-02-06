from .grammar import commandparser
from .model import Entry, Text
from .scope import Scope
import pyparsing, re, traceback

class DanglingStackException(Exception): pass

class NoSuchIndentException(Exception): pass

class MalformedEntryException(Exception): pass

class Repl:

    quotablebysquare = re.compile('[$()]+')

    @classmethod
    def _quote(cls, obj): # TODO: Duplicates some wrap logic.
        for b in map(bool, range(2)):
            if obj is b:
                return str(b).lower()
        try:
            from pathlib import PurePath
            if isinstance(obj, PurePath):
                obj = str(obj)
        except ImportError:
            pass
        try:
            return f"""$.({cls.quotablebysquare.sub(lambda m: f"$'[{m.group()}]", obj)})"""
        except TypeError:
            return obj

    def __init__(self, scope = None, interactive = False, rootprefix = Entry([])):
        self.stack = []
        self.indent = ''
        self.command = Entry([Text(':')])
        self.commandsize = self.command.size()
        self.partials = {'': rootprefix}
        self.scope = Scope() if scope is None else scope
        self.interactive = interactive

    def __enter__(self):
        return self

    def printf(self, template, *args): # TODO: Replace with methods corresponding to directives.
        self(template % tuple(self._quote(a) for a in args))

    def __call__(self, line):
        try:
            suffix = commandparser(''.join(self.stack + [line]))
            del self.stack[:]
        except pyparsing.ParseException:
            self.stack.append(line)
            return
        indent = suffix.indent()
        common = min(len(self.indent), len(indent))
        if indent[:common] != self.indent[:common]:
            raise MalformedEntryException(suffix)
        if len(indent) <= len(self.indent):
            self.fire()
            if indent not in self.partials:
                raise NoSuchIndentException(suffix)
        else:
            self.partials[indent] = self.command
        for i in list(self.partials):
            if len(indent) < len(i):
                del self.partials[i]
        self.command = Entry(self.partials[indent].resolvables + suffix.resolvables)
        self.commandsize = Entry(suffix.resolvables).size()
        self.indent = indent

    def fire(self):
        if self.commandsize:
            try:
                self.scope.execute(self.command)
            except:
                if not self.interactive:
                    raise
                traceback.print_exc(0)

    def __exit__(self, exc_type, *args):
        if exc_type is None:
            if self.stack:
                raise DanglingStackException(self.stack)
            self.fire()
