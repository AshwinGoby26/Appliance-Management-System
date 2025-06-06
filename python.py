import mysql.connector


def get_appliances():
    db = mysql.connector.connect(
        host="127.0.0.1", 
        user="root", 
        password="2005",
        database="gadjets" 
    )
    
    cursor = db.cursor()
    cursor.execute("SELECT * FROM appliances")  
    appliances = cursor.fetchall() 
    for appliance in appliances:
        print(appliance)

    cursor.close()
    db.close()


get_appliances()
