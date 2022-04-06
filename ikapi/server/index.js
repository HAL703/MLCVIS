const express = require('express');
const app = express();
const ImageKit = require('imagekit');

const imagekit = new ImageKit({
  urlEndpoint: 'https://ik.imagekit.io/nd0pfd7urs99',
  publicKey: 'public_9ykx23W51aGNIyoclWqNMQhim/0=',
  privateKey: 'private_699A/t7e8yrWo4Jo3yY0xyL9mBg='
});

// allow cross-origin requests
app.use(function(req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", 
    "Origin, X-Requested-With, Content-Type, Accept");
  next();
});

app.get('/auth', function (req, res) {
  var result = imagekit.getAuthenticationParameters();
  res.send(result);
});

imagekit.listFiles({
    skip : 0,
    limit : 10
}, function(error, result) { 
    if(error) console.log(error);
    else console.log(result);
});

app.listen(3001, function () {
  console.log('Live at Port 3001');
});