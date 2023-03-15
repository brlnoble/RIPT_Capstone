const express = require("express");
const metrics_routes = require("./metrics/routes");

const app = express();
const port = 3000;


// Middleware for handling JSONs
app.use(express.json());

app.get("/", (req, res) => {
    res.send("Hello World!");
});

app.use("/metrics", metrics_routes);

app.listen(port, () => console.log(`app listening on port ${port}!`));