var express = require('express');
var app = express();
var path = require('path');

// viewed at http://localhost:8080


app.use(express.static('public'));

app.get('/', function(req, res) {

    res.sendFile(__dirname + '/index.html');    
    

});
console.log('Server online...')

app.listen(8080);