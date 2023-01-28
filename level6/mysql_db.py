import mysql.connector
class Mysql_DBaccess:
    def __init__(self,host,user,password,db):
        self.host =host
        self.user =user
        self.password =password
        self.db =db
        try:
            self.connection = mysql.connector.connect(host=self.host,user=self.user,password=self.password,database=self.db)
        except :
            print("error while connecting to the database")


    def inser_data(self,filename):
        self.filename=filename

        self.cur=self.connection.cursor()
        sql="insert into files(filename) values(%s);"
        val=(self.filename)

        self.cur.execute(sql,(val,))

        self.connection.commit()
    def search(self):
        self.cur = self.connection.cursor()
        sql = "select *from files limits 0,10;"
        data=self.cur.execute(sql)
        data=self.cur.fetchall()
        return data
    def searchDB(self,fil):

        self.cur=self.connection.cursor()
        sql="""select * from files where filename like '%{0}'""".format(fil)
        self.cur.execute(sql)
        row=self.cur.fetchone()
        if row==0:
            return 0
        else:
            return row

obj=Mysql_DBaccess('localhost','root','Sunayana@447','searchfiles')
obj.inser_data('C:/hcl\\file1.txt')
print(obj.searchDB('file1.txt'))