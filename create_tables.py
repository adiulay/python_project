import sqlite3

conn = sqlite3.connect('maple_story.sqlite')

c = conn.cursor()

c.execute('''
          CREATE TABLE character_list
          (id INTEGER PRIMARY KEY ASC, 
           name VARCHAR(250) NOT NULL,
           job VARCHAR(250) NOT NULL,
           health INTEGER NOT NULL,
           health_regeneration INTEGER NOT NULL,
           attack_damage INTEGER NOT NULL,
           magic_damage INTEGER NOT NULL,
           armor INTEGER NOT NULL,
           magic_resist INTEGER NOT NULL,
           sword VARCHAR(250),
           wand VARCHAR(250),
           spell_cast VARCHAR(250),
           skill_ability VARCHAR(250)
           )
          ''')



conn.commit()
conn.close()