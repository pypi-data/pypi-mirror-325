import sys
from parsearg import ParseArg

def create_user(args):
    print(f'created user: {args.name!r} (email: {args.email}, phone: {args.phone})')
    
def create_todo(args):
    print(f'created TO-DO for user {args.user!r}: {args.title} (due: {args.due_date})')
    
# the CLI "view" comprises pure data: 
#     the parser is fully specified by this view - no imperative instructions are required
view = {
    'create|user': {
        'callback':   create_user,
        'name':       {'help': 'create user name', 'type': str, 'action': 'store'},
        '-e|--email': {'help': "create user's email address", 'type': str, 'action': 'store', 'default': ''},
        '-p|--phone': {'help': "create user's phone number", 'type': str, 'action': 'store', 'default': ''},
    },
    'create|todo': {
        'callback':   create_todo,
        'user':       {'help': 'user name', 'type': str, 'action': 'store'},
        'title':      {'help': 'title of TO-DO', 'type': str, 'action': 'store'},
        '-d|--due-date': {'help': 'due date for the TO-DO', 'type': str, 'action': 'store', 'default': None},
    },
}

def main(args):
    parser = ParseArg(d=view)
    ns     = parser.parse_args(args)
    result = ns.callback(ns)

if __name__ == "__main__":
    args = sys.argv[1:] if len(sys.argv) > 1 else []
    main(' '.join(args))
