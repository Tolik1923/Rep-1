const express = require("express");
const bodyParser = require("body-parser");
const app = express();
const PORT = process.env.API_PORT || 8888;

var { expressjwt: jwt } = require("express-jwt");

app.use(bodyParser.json());

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}.`);
});

app.get("/asset", (req, res) => {
    res.status(200).send("Everybody can see this");
});

const jwtCheck = jwt({
    secret: "Yarynakey",
    algorithms: ["HS256"],

});


app.get("/asset/secret", jwtCheck, (req, res) => {
    res.status(200).send("Only logged in people can see me");
});

app.get("*", (req, res) => {
    res.sendStatus(404);
});

