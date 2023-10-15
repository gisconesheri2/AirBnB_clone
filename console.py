#!/usr/bin/python3
"""console for the entry point of the program"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import json
import re


def add_attribute(search_key, available_insts, args_list):
    """update all instances that are the same as the search key
    with atrributes in the args list
    """

    args_passed = args_list

    if search_key in available_insts:
        obj = available_insts[search_key]
        try:
            # args_passed[2] == attribute name
            value = getattr(obj, args_passed[2])
            try:
                v1 = type(value)(args_passed[3])
                setattr(obj, args_passed[2], v1)
            except ValueError:
                print(f"{args_passed[2]} takes type {type(value)}")
        except AttributeError:
            setattr(obj, args_passed[2], args_passed[3])
        for k, v in available_insts.items():
            storage.new(v)
        storage.save()
    else:
        print("** no instance found **")


class HBNBCommand(cmd.Cmd):
    """console to manage the usage of classes"""

    prompt = "(hbnb) "
    acceptable_classes = ["BaseModel", "User", "State", "City",
                          "Amenity", "Place", "Review"]

    def precmd(self, line):
        """parse line to get a standardized command
        pass it thorough extra processing if in format
        <class name>.command()
        """
        r = re.search(r'(^[A-Za-z]\w+).(\w+)\(([\-"\w\s,{}:\']*)\)', line)
        # r = re.search(r'(^[A-Za-z]\w+).(\w+)\(([{}\-"\w\s,]*)\)', line)
        if r is None:
            return (line)
        else:
            cmd = r.groups()
            line = f"{cmd[1]} {cmd[0]}"
            if (len(cmd[2]) > 0):
                if '{' in cmd[2]:
                    line = line + f" {cmd[2]}"
                    return line
                args = cmd[2].split(',')
                for i in range(len(args)):
                    line = line + f" {args[i]}"
                line = line.replace('"', '')
                return (line)
            else:
                line = f"{cmd[1]} {cmd[0]}"
                return (line)

    def emptyline(self):
        """if an empty line entered, do nothing"""
        pass

    def do_quit(self, line):
        """Quit command to exit program"""
        return True

    def do_count(self, cls):
        """print number of instaces of cls
        Usage: count <class name> / <class name>.count()
        """
        args_passed = cls.split()
        if len(cls.strip()) == 0:
            print("** class name missing **")
        elif args_passed[0] not in HBNBCommand.acceptable_classes:
            print("** class doesn't exist **")
        else:
            ai = storage.all()
            number = 0
            for k, v in ai.items():
                if args_passed[0] == k.split('.')[0]:
                    number += 1
            print(number)

    def do_create(self, cls):
        """creates a new instance of BaseModel and save it to JSON file
        usage: create <class name> / <class name>.create()
        """
        if len(cls.strip()) == 0:
            print("** class name missing **")
        else:
            try:
                new_inst = eval(cls)()
                new_inst.save()
                print(new_inst.id)
            except (NameError, TypeError):
                print("** class doesn't exist **")

    def do_show(self, *args):
        """print a string representation of an instance based
        on class name and id
        usage: show <class name> <instance id>
             : <class name>.show(<instance id>)
        """
        args_passed = args[0].split()
        if len(args_passed) == 0:
            print("** class name missing **")
        elif args_passed[0] not in HBNBCommand.acceptable_classes:
            print("** class doesn't exist **")
        elif len(args_passed) == 1:
            print("** instance id missing **")
        else:
            search_key = f"{args_passed[0]}.{args_passed[1]}"
            available_insts = storage.all()
            if search_key in available_insts:
                print(available_insts[search_key])
            else:
                print("** no instance found **")

    def do_destroy(self, *args):
        """delete an instance based on class name and id
        usage: delete <class name> <instance id>
             : <class name>.destroy(<instance id>)
        """
        args_passed = args[0].split()
        if len(args_passed) == 0:
            print("** class name missing **")
        elif args_passed[0] not in HBNBCommand.acceptable_classes:
            print("** class doesn't exist **")
        elif len(args_passed) == 1:
            print("** instance id missing **")
        else:
            search_key = f"{args_passed[0]}.{args_passed[1]}"
            available_insts = storage.all()
            if search_key in available_insts:
                del available_insts[search_key]
                for k, v in available_insts.items():
                    storage.new(v)
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, args):
        """update an instance based on class name and id
        by updating or adding attribute
        usage: update <class name> <id> <attribute name> "<attribute value>"
             : <class name>.update(<id> <attribute name> "<attribute value>")
             : update <class name> <id> <dictionary represenation>
             : <class name>.update(<id> <dictionary representation>
        """

        dict_present = ''
        dp = 0
        args_passed = []
        try:
            # look for a dictionary
            start_idx = args.rindex('{')
            end_idx = args.rindex('}')
            dict_present = args[start_idx: end_idx + 1]
            args = args[:start_idx]
            args = args.replace('"', '')
            args = args.replace(',', '')
            args_passed = args.split()
            args_passed.append('dict')
            dp = 1
        except ValueError:
            args1 = args.replace('"', '')
            args_passed = args1.split()
        if len(args_passed) == 0:
            print("** class name missing **")
        elif args_passed[0] not in HBNBCommand.acceptable_classes:
            print("** class doesn't exist **")
        elif len(args_passed) == 1:
            print("** instance id missing **")
        elif len(args_passed) == 2:
            print("** attribute name missing **")
        elif len(args_passed) == 3:
            if dp == 1:
                dict_present = dict_present.replace("'", '"')
                dict_p = json.loads(dict_present)
                search_key = f"{args_passed[0]}.{args_passed[1]}"
                available_insts = storage.all()
                for k, v in dict_p.items():
                    args_list = args_passed[0:2]
                    args_list.append(k)
                    args_list.append(v)
                    add_attribute(search_key, available_insts, args_list)
            else:
                print("** value missing **")
        else:
            search_key = f"{args_passed[0]}.{args_passed[1]}"
            available_insts = storage.all()
            add_attribute(search_key, available_insts, args_passed)

    def do_all(self, args):
        """print a list of strings of the string represenation of all
        instances based on the class provided or all instances on file
        usage: all or all <class name> or <class name>.all()
        """
        args_passed = args.split()
        if len(args_passed) == 0:
            ai = storage.all()
            str_rep_list = []
            for v in ai.values():
                str_rep_list.append(v.__str__())
            print(str_rep_list)
        elif args_passed[0] not in HBNBCommand.acceptable_classes:
            print("** class doesn't exist **")
        else:
            ai = storage.all()
            str_rep_list = []
            for k, v in ai.items():
                if args_passed[0] == k.split('.')[0]:
                    str_rep_list.append(v.__str__())
            print(str_rep_list)

    def do_EOF(self, line):
        """end of file (ctrl-d) handler"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
