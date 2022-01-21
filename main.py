from db_connection import connect_db
from phase12.phase12 import run_phase12

if __name__ == '__main__':
    db, cursor = connect_db()
    run_phase12(db, cursor)


