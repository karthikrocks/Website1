var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "karthi@0709",
  database: "karthikDB"
});
class db {
  constructor(name, email, password) {
    this.name = name;
    this.email = email;
    this.password = password;
  }
  TestConnection() {
    con.connect(function(err) {
      if (err) throw err;
      console.log("Connected!");
    });
  }
  createDB() {
    con.connect(function(err) {
      if (err) throw err;
      console.log("Connected!");
      con.query("CREATE DATABASE jsdb", function (err, result) {
        if (err) throw err;
        console.log("Database created");
      });
    });
  }
  createTable() {
    con.connect(function(err) {
      if (err) throw err;
      console.log("Connected!");
      var sql = "Create  table User(userId integer, username varchar(200), email varchar(200), passwd varchar(200))";
      con.query(sql, function (err, result) {
        if (err) throw err;
        console.log("Table created");
      });
    });
  }
  AddUser(name, email, passwd) {
    con.connect(function(err) {
      if (err) throw err;
      console.log("Connected!");
      var sql = "Insert into user(username, email, passwd) values('" + name + "', " + "'" + email + "', " + "'" + passwd + "')";
      con.query(sql, function (err, result) {
        if (err) throw err;
        console.log("User created");
      });
    });
  }
  DeleteUser(email) {
    con.connect(function(err) {
      if (err) throw err;
      console.log("Connected!");
      var sql = "DELETE FROM user WHERE email='" + email + "'";
      con.query(sql, function (err, result) {
        if (err) throw err;
        console.log("User deleted");
      });
    });
  }
}
module.exports = db, con
DB = new db();

// Driver Code...
// console.log(DB.AddUser("Karthiks", "test@test", "1234"))
// console.log(DB.DeleteUser("test@test"))