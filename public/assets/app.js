function openBox(selector) {
    document.querySelector(selector).open = true
}

const socket = io("", {
    path: '/socket.io',
    transports: ['websocket'],
    secure: true,
})

let terminal = document.querySelector("#terminal")

document.querySelector(".c").addEventListener("submit", (e) => {
    e.preventDefault()
    let obj = {
        application: e.target.application.value
    }

    let command = e.target.command.value.split("@")
    obj["command"] = command[0]
    obj["filename"] = command[1] || "uploaded_file"

    let f = `${command[1] == undefined ? "" : "<@>" + obj.filename}`
    if (command[0].length > 0) {
        setCommand(obj)
        terminalBox(0, `> ${obj.application}: ${obj.command}${f}`)
    }
})


function terminalBox(s, text) {
    if (s == 0) {
        className = "l0"
    } else if (s == 1) {
        className = "l1"
    } else {
        className = ""
    }
    const pre = document.createElement("pre")
    pre.innerText = text
    pre.className = className
    terminal.appendChild(pre)

    terminal.scrollTop = terminal.scrollHeight
}

function setCommand(obj) {
    axios.post(`/panel/command?id=${ID}`, obj, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    }).then(res => {
        if (res.data == "OK") {
            document.querySelector(".c input").value = ""
        }
    })
}

socket.on(ID, data => {
    console.log(data)
    if (data == "exit status 1") {
        terminalBox(1, data)
    } else {
        terminalBox(3, data)
    }
})

let index = 0
socket.on(ID + "-on", data => {
    index += 1
    document.querySelector("#indicate").innerHTML = `${index} PING`
})

let commandsContent = document.querySelector(".commands")
let cHtml = ""
for (let c of dataCommands) {
    cHtml += `
    <p>
    <button class="c-btn" application="${c[0]}" command="${c[1]}"><i class="material-icons">code</i></button> 
    <span><b>${c[0].toUpperCase()}</b> : ${c[2]}</span>
    </p>`
}
commandsContent.innerHTML += cHtml

commandsContent.querySelectorAll(".c-btn").forEach(btn => {
    btn.addEventListener("click", () => {
        commandsContent.open = false
        document.querySelector(".c select").value = btn.getAttribute("application")
        document.querySelector(".c input").value = btn.getAttribute("command")
    })
})