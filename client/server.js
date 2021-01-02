const express = require('express');
var cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const port = process.env.PORT || 5000;
const { Client } = require('pg')
const client = new Client({
    user: 'admin',
    host: 'localhost',
    database: 'my_internet',
    password: 'passpass1234!',
    port: 5432,
})

app.get('', (req, res) => {
    console.log('Hello world!') // Hello world!
    res.send({ express: 'API моего интернета' });
});

app.post('/api/login', (req, res) => {
    /*
    client.connect()
    client.query('SELECT token FROM core_person where ')
        .then(res => console.log(res.rows[0]))
        .catch(e => console.error(e.stack))
    console.log(req.body);
    */
    res.send({access_token: "f400cb32-50ee-44e5-8e1d-492637e7945f"});
});

app.listen(port, () => console.log(`Listening on port ${port}`));