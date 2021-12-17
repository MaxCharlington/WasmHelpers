const express = require('express')
const app = express()
const port = 3000

app.get('/compile', (req, res) => {
    res.send(req.body)
})

app.listen(port, () => {
  console.log(`Listening at http://localhost:${port}`)
})
