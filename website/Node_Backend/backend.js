
const express = require('express')
const request = require('request');

app = express();
const PORT = 3000;

app.get('/login_register', function(req, res) {
    request('http://192.168.1.27:1000/login-register', function (error, response, body) {
        console.error('error:', error); // Print the error
        console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
        console.log('body:', body); // Print the data received
        res.send(body); //Display the response on the website
      });
});

app.listen(PORT, function (){
    console.log('Listening on Port 3000');
});
