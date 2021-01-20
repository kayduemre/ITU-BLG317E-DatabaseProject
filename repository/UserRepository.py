from services.database import Database

def getUsers():
    db = Database().getDatabaseInstance()
    cursor = db.cursor()

    query = """SELECT * FROM USERS """
    cursor.execute(query)
    users = cursor.fetchall()
    return users

def sendFeedBack(feedback):
    db = Database().getDatabaseInstance()
    cursor = db.cursor()
    data = feedback.dic()

    query = "INSERT INTO FEEDBACKS (PROTECT, RELIABILITY, DELIVERY, USER_ID) VALUES(%(protect)s, %(reliability)s,%(delivery)s, %(user_id)s)  RETURNING id"
    cursor.execute(query,data)
    db.commit()
    feed_id = cursor.fetchone()
    

    query = "SELECT SUM(PROTECT)/COUNT(id), SUM(DELIVERY)/COUNT(ID), SUM(RELIABILITY)/COUNT(ID) FROM FEEDBACKS WHERE USER_ID = %s"
    id = str(data['user_id'])
    cursor.execute(query,(id,))
    val = cursor.fetchall()
    total = sum(val[0])/3
    
    query = "UPDATE FEEDBACKS SET VOTE = %s WHERE (ID = %s)"
    cursor.execute(query,(total,feed_id,))
    db.commit()
    
