from tinydb import TinyDB, Query, where
import sys

DB_PATH = "db.json"

def main():
    db = TinyDB(DB_PATH)
    token_table = db.table("tokens")

    args = sys.argv[1:]
    if args[0] == 'add':
        i = 1
        while i < len(args):
            token_table.insert({"token": args[i]})
            i += 1
        return
    if args[0] == 'rm':
        i = 1
        while i < len(args):
            token_table.remove(where("token")==args[i])
            i += 1
        return
    if args[0] == 'ls':
        for token in token_table.all():
            print(token["token"])

if __name__ == "__main__":
    main()
        