import pymysql.cursors

# Function return a connection.
def getConnection():
    try:
        connection = pymysql.connect(host="localhost",
                               user="root",
                               passwd="password",
                               db="algotreading",
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)
    except pymysql.Error as error:
        print(error)

    return connection

if __name__ == '__main__':
    getConnection()