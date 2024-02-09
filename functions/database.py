import sqlite3

class Database:
    def __init__(self, database_name: str) -> None:
        self.database = sqlite3.connect(database_name)
        self.database.row_factory = sqlite3.Row
        self.database.execute('CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, content TEXT NOT NULL)')

    def __del__(self) -> None:
        self.database.close()

    def createTestPost(self) -> None:
        self.database.execute('INSERT INTO posts (title, content) VALUES ("Random Title", "Lorem ipsum dolor sit amet consectetur adipiscing elit")')