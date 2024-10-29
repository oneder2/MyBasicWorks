import pymysql


connector = 0
myCursor = 0

# commit & rowback
try:
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
    # submit
    myCursor.execute(sql)
    connector.commit()

except Exception as e:
    # row back
    print(f"There is {e} in SQL code.")
    if connector != 0:
        connector.rollback()

finally:
    print(connector)
    if connector != 0 and myCursor != 0:
        # memory safty: close the connector & cursor
        myCursor.close()
        connector.close()
