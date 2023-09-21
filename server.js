const express = require("express")
const app = express()
const fileUpload = require("express-fileupload")
const server = require("http").createServer(app)
const io = require("socket.io")(server)
const cookieParser = require("cookie-parser")
const { JSONStorage } = require("node-localstorage")
const ssd = new JSONStorage("./ssd")


JSONStorage(`${process.cwd()}/public/ssd/uploads`)
JSONStorage(`${process.cwd()}/public/ssd/book`)
app.use(fileUpload())
app.use(cookieParser())
app.use(express.static(process.cwd() + "/public"))
app.use(express.urlencoded({ extended: false }))
app.set("view engine", "ejs")
app.use(function (req, res, next) {
    req.auth = ssd.getItem("config.json")
    req.io = io
    next()
})

app.use("/", require("./route/dash"))
app.use("/target", require("./route/target"))
app.use(checkToken)
app.use("/panel", require("./route/panel"))
app.use("/terminal", require("./route/terminal"))

function checkToken(req, res, next) {
    let token = req.cookies.token
    if (token != undefined && token == req.auth["token"]) {
        next()
    } else {
        res.clearCookie("token")
        res.redirect("/")
    }
}

const PORT = process.env.PORT || 9411
server.listen(PORT, () => {
    console.log(`PORT IS : ${PORT}
    > You want to change the password of blackpanther
    > EDIT ${process.cwd()}/ssd/config.json
    `)
})