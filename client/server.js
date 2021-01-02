const express = require('express');
var cors = require('cors');
const bodyParser = require('body-parser');
const app = express();
app.use(cors());
const port = process.env.PORT || 5000;
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const { Client } = require('pg')
const client = new Client()

app.get('', (req, res) => {
    console.log('Hello world!') // Hello world!
    res.send({ express: 'API моего интернета' });
});

app.post('/api/login', (req, res) => {
    console.log(req.body);
    res.send(
        `I received your POST request. This is what you sent me: ${req.body.post}`,
    );
});

app.listen(port, () => console.log(`Listening on port ${port}`));