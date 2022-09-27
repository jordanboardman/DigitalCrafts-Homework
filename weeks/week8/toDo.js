const express = require("express");
const app = express();
const logger = require("./logger");
let todo = require("./database");
const ejs = require("ejs");
const pg = require("pg-promise")(); //saying "this package requires pg promise" and also instantiating it with the second set of ()
const db = pg("postgres://jordanboardman@localhost:5432/jordanboardman"); // accessing our todoDB from postgreSQL
app.use(express.json());
app.set("view engine", "ejs");

// ---------------------------------------------
// ALL methods

app.all("*", (req, res, next) => {
  // next tells the computer that we're gonna go to the next function according to whatever the end point is called (so if there are 2 GET calls, it'll recognize both)
  logger.info({
    action: req.method,
    path: req.path,
    body: req.body,
    time: new Date(),
  });
  next();
});
// ---------------------------------------------
// GET methods
// Client gets full todo list
// To use: just type '/' after base URL with no body
app.get("/", function (req, res) {
  if (Object.keys(req.body).length === 0) {
    db.any("SELECT * FROM tododb").then((fulltodolist) => {
      logger.info({
        status_code: res.statusCode,
        res_body: fulltodolist,
        time: new Date(),
      });

      res.send(fulltodolist);
    });
  } else {
    // log error in logger here
    res.statusCode = 400;
    res.send("GET requests do not take body parameters.");
  }
});

// Client gets specific todo item
// To use: after '/todo', type '?number=' and the # you want
app.get("/todo", function (req, res) {
  let match = false;
  let task = req.query.number;

  db.oneOrNone(`SELECT * FROM tododb WHERE number = $1`, task).then(
    (todoitem) => {
      //selecting all Pokemon from the database
      logger.info({
        status_code: res.statusCode,
        res_body: todoitem,
        time: new Date(),
      });

      res.send(todoitem);

      // for (let i = 0; i < todo.length; i++) {
      //   if (todo[i].number == task && Object.keys(req.body).length === 0) {
      //     console.log("inside for loop");
      //     match = true;
      //     number = todo[i].number;
      //     res.send(todo[i]);
      //   } else if (todo[i].number != task) {
      //     res.statusCode = 400;
      //     res.send("Task number not in list.");
      // } else {
      //   console.log("inside else statement");
      //   res.statusCode = 400;
      //   res.send("GET requests do not take body parameters.");
      // }
    }
  );
});
// ---------------------------------------------
// POST method

app.post("/todo/", function (req, res) {
  db.any(`INSERT INTO tododb (number, chore) VALUES ($1, $2)`, [
    req.body.number,
    req.body.chore,
  ]).then((fulltodolist) => {
    //selecting all Pokemon from the database
    logger.info({
      status_code: res.statusCode,
      res_body: fulltodolist,
      time: new Date(),
    });

    res.send(fulltodolist);
  });
});

//   newTodo = { number: req.body.number, chore: req.body.chore };
//   if (typeof newTodo.number != "number") {
//     // check if the number is of the type 'number'
//     res.statusCode = 400;
//     res.send("Task item is invalid");
//   } else if (typeof newTodo.chore != "string") {
//     // check if the chore is a string
//     res.statusCode = 400;
//     res.send("Chore type is invalid");
//   }
//   // else if(todo.includes(newTodo.number,todo.number.length)){
//   //     res.statusCode = 400
//   //     res.send(`List item already exists. Here is a list of your to-dos: ${todo}.`)
//   // }
//   else {
//     todo.push(newTodo);
//     res.send(
//       `You created the to-do item ${newTodo.chore}. It is item number ${newTodo.number} on your list.`
//     );
//   }
// });
// ---------------------------------------------
// PUT method
app.put("/todo/", async (req, res) => {
  let match = false;
  let task = req.body.number;
  let toDo = req.body.chore;
  let updatedToDo = {};

  await db
    .oneOrNone(`UPDATE tododb SET chore = $1 WHERE number = $2`, [
      req.body.chore,
      req.body.number,
    ])
    .then((updatedToDo) => {
      logger.info({
        status_code: res.statusCode,
        res_body: updatedToDo,
        time: new Date(),
      });
    });

  db.oneOrNone(`SELECT * FROM tododb WHERE number = $1`, task).then(
    (result) => {
      res.send(result);
    }
  );

  // if (typeof task != "number") {
  //   // check if the number is of the type 'number'
  //   res.statusCode = 400;
  //   res.send("Task item is invalid");
  // } else if (typeof toDo != "string") {
  //   // check if the chore is a string
  //   res.statusCode = 400;
  //   res.send("Chore type is invalid");
  // } else {
  //   for (let i = 0; i < todo.length; i++) {
  //     if (todo[i].number == task) {
  //       match = true;
  //       todo[i].chore = toDo;
  //       updatedToDo = todo[i];
  //       res.send(updatedToDo);
  //     }
  //   }
  // }

  // if (todo.indexOf(task) === -1 && match == false) {
  //   res.statusCode = 400;
  //   res.send("List item does not exist.");
  // }
});
// ---------------------------------------------
// DELETE method

app.delete("/todo/:number", function (req, res) {
  db.oneOrNone(` DELETE FROM tododb WHERE number = $1`, task).then(
    (todoitem) => {
      //selecting all Pokemon from the database
      logger.info({
        status_code: res.statusCode,
        res_body: todoitem,
        time: new Date(),
      });

      // res.send(todoitem);

      if (Object.keys(req.body).length === 0) {
        let match = false;
        let task = req.params.number;

        for (let i = 0; i < todo.length; i++) {
          if (todo[i].number == task) {
            match = true;
            deletedChore = todo[i];
            // before we actually delete the object of the chore we want to delete, change the value of the succeeding objects' "number" to -1
            // for(let j = i + 1; j < todo.length; j++) {
            //     updatedList = todo[j].number -= 1
            //     todo.push(updatedList)
            // }
            todo.splice(i, 1);
            res.send(deletedChore);
            todo.number -= 1;
          }
        }

        if (match == false) {
          res.statusCode = 400;
          res.send("List item does not exist.");
        }
      } else {
        res.statusCode = 400;
        res.send("DELETE requests do not take body parameters.");
      }
    }
  );
  // ---------------------------------------------

  port = 3000;
  app.listen(port);
  console.log(`Server is running on port ${port}`);
});
