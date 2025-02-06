import sys
import argparse

def create_user(args):
    print(f'created user: {args.name!r} (email: {args.email}, phone: {args.phone})')
    
def create_todo(args):
    print(f'created TO-DO for user {args.user!r}: {args.title} (due: {args.due_date})')
    
def make_parser():
    # Imperative instructions are required to construct the CLI 
    parser            = argparse.ArgumentParser()
    subparsers        = parser.add_subparsers()

    create            = subparsers.add_parser('create')
    create_subparsers = create.add_subparsers()

    user              = create_subparsers.add_parser('user')
    todo              = create_subparsers.add_parser('todo')

    user.add_argument("name", help="create user name", type=str, action="store")
    user.add_argument("-e", "--email", help="create user's email address", type=str, action="store", default='')
    user.add_argument("-p", "--phone", help="create user's phone number", type=str, action="store", default='')
    user.set_defaults(callback=create_user)

    todo.add_argument("user", help="user name for TO-DO", type=str, action="store")
    todo.add_argument("title", help="title of TO-DO", type=str, action="store")
    todo.add_argument("-d", "--due-date", help="due date for the TO-DO", type=str, action="store", default=None)
    todo.set_defaults(callback=create_todo)

    return parser

def main(args):
    parser = make_parser()
    ns     = parser.parse_args(args)
    result = ns.callback(ns)

if __name__ == "__main__":
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    main(args)
