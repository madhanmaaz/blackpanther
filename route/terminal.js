const express = require("express")
const app = express.Router()
const { LocalStorage } = require("node-localstorage")
const fs = require("fs")

app.route("/").get((req, res) => {
    let data = fs.readdirSync(`${process.cwd()}/public/ssd/book/`)
    res.send(data)
}).post((req, res) => {
    let id = req.query.id
    const book = new LocalStorage("./public/ssd/book")
    let command = ""
    for (let key in req.body) {
        command += req.body[key] + "\n"
    }

    book.setItem(id, command)
    res.send("OK")
})


module.exports = app