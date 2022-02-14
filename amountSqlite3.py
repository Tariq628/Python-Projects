import sqlite3
con = sqlite3.connect("fisrtdb.db")
cur = con.cursor()
con.commit()
# cur.execute("create table tariq(id int primary key not null, name varchar(100), balance int)")
# cur.execute("insert into tariq('id', 'author', 'book') values(4, 'tariq', 'Python')")

# cur.execute("insert into tariq values(?,?,?)", (1, 'Tariq', 1000))
# cur.execute("insert into tariq values(?,?,?)", (2, 'Tariq', 1000))
class Bank:
    def withdrawamount(self, Id, name, balance):
        cur.execute("select * from tariq where id=? and name=?", (Id, name))
        self.bal = 0
        for i in cur:
            self.bal = i[2]
        if balance <= self.bal:
            print(f"Take your Amount {balance} Thank You.. Your Remaining Amount is {self.bal-balance}")
            cur.execute("update tariq set balance=? where Id=? and name=?", (self.bal - balance, Id, name))
        else:
            print("You don't have sufficient Amount")

    def deposit(self):
        pass
    def showdetail(self, name, Id):
        # cur.execute("select * from tariq where id=4 and book='Python'")
        cur.execute("select * from tariq where id=? and name=?", (Id, name))
        for i in cur:
            print(i)
bank = Bank()
bank.showdetail("Tariq", 1)
bank.withdrawamount(1, "Tariq", 50)
con.commit()
con.close()
