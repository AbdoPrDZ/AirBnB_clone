#!/usr/bin/python3

from cmd import Cmd
import sys

import models
from models.base_model import BaseModel


class HBNBCommand(Cmd):

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        exit(0)

    def do_EOF(self, arg):
        """Quit command to exit the program"""
        self.do_quit(arg)

    def emptyline(self):
        pass

    def do_create(self, arg):
        if not arg:
            return print("** class name missing **", file=sys.stderr)

        if not arg in models.CLASSES.keys():
            return print("** class doesn't exist **", file=sys.stderr)

        _class = models.CLASSES[arg]

        obj = _class()
        obj.save()

        print(obj.id)

    def do_show(self, arg):
        args = arg.split()

        if len(args) < 1:
            return print("** class name missing **", file=sys.stderr)

        if not args[0] in models.CLASSES.keys():
            return print("** class doesn't exist **", file=sys.stderr)

        if len(args) < 2:
            return print("** instance id missing **", file=sys.stderr)

        id = (
            args[1][1:-1]
            if len(args[1]) >= 2 and args[1][0] == '"' and args[1][-1] == '"'
            else args[1]
        )
        id = "{class_name}.{id}".format(class_name=args[0], id=id)

        all = models.storage.all()

        if not id in all.keys():
            return print("** no instance found **", file=sys.stderr)

        print(all[id])

    def do_destroy(self, arg):
        args = arg.split()

        if len(args) < 1:
            return print("** class name missing **", file=sys.stderr)

        if not args[0] in models.CLASSES.keys():
            return print("** class doesn't exist **", file=sys.stderr)

        if len(args) < 2:
            return print("** instance id missing **", file=sys.stderr)

        id = (
            args[1][1:-1]
            if len(args[1]) >= 2 and args[1][0] == '"' and args[1][-1] == '"'
            else args[1]
        )
        id = "{class_name}.{id}".format(class_name=args[0], id=id)

        all = models.storage.all()

        if not id in all.keys():
            return print("** no instance found **", file=sys.stderr)

        del all[id]
        models.storage.save()

    def do_all(self, arg):
        if not arg:
            return print("** class name missing **", file=sys.stderr)

        if not arg in models.CLASSES.keys():
            return print("** class doesn't exist **", file=sys.stderr)

        _class = models.CLASSES[arg]

        all = _class.all()

        items = []

        for item in all:
            items.append(str(item))

        print(items)

    def do_count(self, arg):
        if not arg:
            return print("** class name missing **", file=sys.stderr)

        if not arg in models.CLASSES.keys():
            return print("** class doesn't exist **", file=sys.stderr)

        _class = models.CLASSES[arg]

        all = _class.all()

        print(len(all))

    def do_update(self, arg):
        args = arg.split()

        if len(args) < 1:
            return print("** class name missing **", file=sys.stderr)

        if not args[0] in models.CLASSES.keys():
            return print("** class doesn't exist **", file=sys.stderr)

        if len(args) < 2:
            return print("** instance id missing **", file=sys.stderr)

        id = (
            args[1][1:-1]
            if len(args[1]) >= 2 and args[1][0] == '"' and args[1][-1] == '"'
            else args[1]
        )
        id = "{class_name}.{id}".format(class_name=args[0], id=id)

        all = models.storage.all()

        if not id in all.keys():
            return print("** no instance found **", file=sys.stderr)

        obj = all[id]

        if len(args) < 3:
            return print("** attribute name missing **", file=sys.stderr)

        line = " ".join(args[2:])
        name = ""
        value = ""

        if '"' in line:
            i, j = 0, 0
            insideQuote = False
            while i < len(line):
                c = line[i]

                if c == " " and not insideQuote and len([name, value][j]) == 0:
                    i += 1
                    continue
                elif c == '"':
                    if i == 0 or not insideQuote:
                        insideQuote = True
                        i += 1
                        continue
                    elif insideQuote:
                        if i == len(line) - 1:
                            break
                        else:
                            insideQuote = False
                            i += 1
                            j += 1
                            continue

                elif c == "\\" and i + 1 < len(line) and line[i + 1] == '"':
                    c = '"'
                    i += 1

                if j == 0:
                    name += c
                elif j == 1:
                    value += c
                i += 1
        else:
            name = args[2]
            value = args[3] if len(args) >= 4 else ""

        if not value:
            return print("** value missing **", file=sys.stderr)

        print(id, name, value)

        if not name in BaseModel.UNCHANGEABLE_ATTRS:
            setattr(obj, name, value)

            obj.save()

    def default(self, line):
        if "." in line:
            _class = line.split(".")[0]

            if not _class in models.CLASSES.keys():
                return print("** class doesn't exist **", file=sys.stderr)

            line = ".".join(line.split(".")[1:])

            if "(" in line and line[-1] == ")":
                func = line.split("(")[0]

                if func == "all":
                    return self.do_all(_class)
                elif func == "count":
                    return self.do_count(_class)
                else:
                    args = line[len(func) + 1 : -1].split(", ")

                    if func == "show":
                        return self.do_show(
                            "{_class} {id}".format(_class=_class, id=args[0])
                        )
                    elif func == "destroy":
                        return self.do_destroy(
                            "{_class} {id}".format(_class=_class, id=args[0])
                        )
                    elif func == "update":
                        id = args[0]

                        updates = []

                        if len(args) >= 2 and args[1][0] == "{":
                            _dict = ""
                            arg = ", ".join(args[1:])
                            cc = 0

                            for c in arg:
                                if c == "{":
                                    cc += 1
                                elif c == "}":
                                    if cc > 0:
                                        cc -= 1
                                    else:
                                        _dict += c
                                        break
                                _dict += c

                            try:
                                _dict = eval(_dict)

                                for name in _dict:
                                    updates.append(
                                        [
                                            id,
                                            name,
                                            _dict[name],
                                        ]
                                    )
                            except Exception as e:
                                return print(
                                    "Error: Usage: <class name>.update(<id>, <dictionary representation>)",
                                    file=sys.stderr,
                                )
                        else:
                            updates = [
                                [
                                    id,
                                    args[1] if len(args) >= 2 else "",
                                    args[2] if len(args) >= 3 else "",
                                ]
                            ]

                        for id, name, value in updates:
                            self.do_update(
                                "{_class} {id} {name} {value}".format(
                                    _class=_class, id=id, name=name, value=value
                                )
                            )
                        return

        print("*** Unknown syntax: " + line)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
