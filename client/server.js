const express = require('express');
var cors = require('cors');
const bodyParser = require('body-parser');

const app = express();
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const port = process.env.PORT || 5000;
const { Client, Pool } = require('pg')
const client = new Client({
    user: 'admin',
    host: 'localhost',
    database: 'my_internet',
    password: 'passpass1234!',
    port: 5432,
});

app.get('', (req, res) => {
    console.log('Hello world!') // Hello world!
    res.send({ express: 'API моего интернета' });
});

app.post('/api/login', (req, res) => {
    const sql = "SELECT * FROM core_person WHERE username = '$1' AND password = '$2'";
    //console.log('request is ', req, ' res is ', res);
    client.query(sql, ['test_user', 'test_user']).then(res => {
        if (res.rows.length > 0) {
            //console.log('the rows are', res.rows);
            res.send({access_token: res.rows[0]});
        } else {
            res.send({error: "Неверный логин или пароль"})
        }
    }).catch(res => {
        res.send({error: "Внутренняя ошибка сервера"})
    });
});

app.listen(port, '0.0.0.0');
console.log('listening on all availiable interfaces');