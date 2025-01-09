// Step1: 安装express
// npm install express
// Step2: 运行
// node node_js.js

const hostname = '127.0.0.1';
const port = 3000;

// 方法1: http (不需要express)
const http = require('http'); // http模块是内置模块，不用去install

const server = http.createServer((req, res) => {
  if (req.url === '/hello' && req.method === 'GET') {
    res.writeHead(200, { 'Content-Type': 'text/plain' });
    res.end('Hello World');
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('Not Found');
  }
});

server.listen(port, hostname, () => {
  console.log('Server running on http://localhost:3000');
});

// 方法2: express
// const express = require('express');
// const app = express();

// app.get('/hello', (req, res) => {
//   res.send('Hello World2');
// });

// app.listen(port, hostname,() => {
//   console.log('Server running on http://localhost:3000');
// });
