const express = require("express")
const app = express.Router()
const fs = require("fs")

app.route("/").get((req, res) => {
    const token = req.cookies.token
    if (token && token == req.auth["token"]) {
        let data = fs.readdirSync(`${process.cwd()}/public/ssd/book/`)
        res.render("dash", {
            data
        })
    } else {
        res.render("login")
    }
}).post((req, res) => {
    const { p1, p2 } = req.body
    if (p1 == req.auth["username"] && p2 == req.auth["password"]) {
        res.cookie("token", req.auth["token"])
        res.redirect("/")
    } else {
        res.redirect("/")
    }
})

app.get("/close", (req, res) => {
    res.send("server stoping....")
    process.exit(0)
})

module.exports = app