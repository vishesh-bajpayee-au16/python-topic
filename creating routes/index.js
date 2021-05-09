const express = require("express");
const app = express();
app.use(express.json());

app.get("/", (req, res) => {
  res.send("This is Home Page");
});

app.get("/:category", (req, res) => {
  res.send(`Category: ${req.params.category} logged `);
  console.log(req.params);
});

app.get("/:category/:subCategory", (req, res) => {
  res.send(`Sub category: ${req.params.subCategory} logged`);
  console.log(req.params);
});

app.post("/", (req, res) => {
  console.log(req.body);
  //   res.send(`Your Name is ${req.body.name} and your age is ${req.body.age}`);

  const newData = { ...req.body };
  newData.skill = "programming";
  res.json(newData);
  
});

app.listen(3000, () => console.log("Server Started"));
