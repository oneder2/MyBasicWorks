import pymysql


connector = pymysql.Connect(host = '127.0.0.1', 
                            port = 3307, 
                            user = 'learner', 
                            password = '1q@W3e$R5t^Y',
                            database = 'test'
                            )

myCursor = connector.cursor()

# if primary key || auto_increment
# sql = 'INSERT INTO student VALUES (null, "Gellar", 18)'
sql = 'INSERT INTO student(name) VALUES ("Gellar")'

myCursor.execute(sql)

connector.commit()

# memory safty: close the connector & cursor
myCursor.close()
connector.close()



