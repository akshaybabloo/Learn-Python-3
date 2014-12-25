import sqlite3

def main():
    db = sqlite3.connect('test.db')
    
    db.row_factory = sqlite3.Row # converts tuples to objects
    
    # regular sql statements
    db.execute('drop table if exists test')
    db.execute('create table test (t1 text, i1 int)')
    db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
    db.execute('insert into test (t1, i1) values (?, ?)', ('two', 2))
    db.execute('insert into test (t1, i1) values (?, ?)', ('three', 3))
    db.commit()
    
    cursor = db.execute('select * from test order by t1')
    
#     for row in cursor:
#         print(row)
    
#     for row1 in cursor:
#         print(dict(row1))

    for row2 in cursor:
        print(row2['t1'], row2['i1'])
        
if __name__ == '__main__': main()