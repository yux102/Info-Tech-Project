var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
const port = process.env.PORT || 3000;
const processMessage = require('./process-message');

app.use('/frontend', express.static('frontend'));
app.use('/pdfs', express.static('pdfs'));

app.get('/', function (req, res) {
	res.sendFile(__dirname + '/index.html');
});

io.on('connection', function (socket) {
	socket.on('user message', function (msg) {
		io.emit('user message', msg);
		// io.emit('chat message', processMessage(msg));
		// processMessage(msg);
		requestDialogflow(msg);
	});
});

http.listen(port, function () {
	console.log('listening on *:' + port);
});

async function requestDialogflow(msg) {
	var processedMessage = await processMessage(msg);
	io.emit('bot message', processedMessage);
}