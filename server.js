const crypto = require('crypto');
const {execSync} = require('child_process')
const express = require('express')
const fs = require('fs');

const app = express()

app.use(express.static('public'));

app.use(function(req, res, next) {
    req.rawBody = ''
    req.setEncoding('utf8')

    req.on('data', function(chunk) {
      req.rawBody += chunk
    })

    req.on('end', function() {
        next();
    });
});

const port = 3000

app.put('/compile', (req, res) => {
    const hash = crypto.createHash('md5').update(req.rawBody).digest('hex');
    const path = `compiled/${hash}.js`
    if (!fs.existsSync(path)) {
        const tmpFilePath = `tmp/${hash}.cpp`
        fs.writeFileSync(tmpFilePath, req.rawBody, err => {
            if (err) {
                console.error(err);
            }
        })
        execSync(`npm run compile -- ${tmpFilePath}`)
    }
    res.send(path)
})

app.listen(port, () => {
    console.log(`Listening at http://localhost:${port}`)
})
