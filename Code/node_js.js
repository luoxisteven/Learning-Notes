const hostname = '127.0.0.1';
const port = 3000;

// http模块是内置模块，不用去install
// const http = require('http');

// const server = http.createServer((req, res) => {
//   if (req.url === '/hello' && req.method === 'GET') {
//     res.writeHead(200, { 'Content-Type': 'text/plain' });
//     res.end('Hello World');
//   } else {
//     res.writeHead(404, { 'Content-Type': 'text/plain' });
//     res.end('Not Found');
//   }
// });

// server.listen(port, hostname, () => {
//   console.log('Server running on http://localhost:3000');
// });


// npm install express
const express = require('express');
const app = express();

app.get('/hello', (req, res) => {
  res.send('Hello World2');
});

app.listen(port, hostname,() => {
  console.log('Server running on http://localhost:3000');
});
