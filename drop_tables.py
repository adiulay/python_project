import sqlite3

conn = sqlite3.connect('maple_story.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE character_list
          ''')

conn.commit()
conn.close()
