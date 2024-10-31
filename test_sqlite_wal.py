from dissect.sql import sqlite3
import os
from pathlib import Path
from pprint import pprint

db_path = Path("/home/user/GIT/data/sqlitewal_testdb")
wal_path = Path("/home/user/GIT/data/sqlitewal_testdb-wal")

db_path = Path("/home/user/GIT/data/sqlite_wal_test.sqlite3")
wal_path = Path("/home/user/GIT/data/sqlite_wal_test.sqlite3-wal")


def test_sqlite_wal():
    db = sqlite3.SQLite3(db_path.open("rb"), wal_path.open("rb"))

    for table in db.tables():
        pprint(list(table))

    print("")

    for check in db.wal.checkpoints:
        print(check)
        print(check.root_page_map)
        checkpoint_db = sqlite3.SQLite3(db_path.open("rb"), wal_checkpoint=check)
        for table in checkpoint_db.tables():
            pprint(list(table))
            print("")

    # for frame in db.wal.frames():
    #     print(frame.page)
    #     for cell in frame.page.cells():
    #         # print(cell, cell.values)


if __name__ == "__main__":
    test_sqlite_wal()
