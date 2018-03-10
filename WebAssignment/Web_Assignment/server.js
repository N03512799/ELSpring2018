
var express = require('express');

var app = express();
var server = app.listen(12001);

app.use(express.static('public'));


console.log("My socket server is running!!");

var socket = require('socket.io');

var io = socket(server);

io.sockets.on('connection', newConnection);

var PythonShell = require('python-shell');

function newConnection(socket){
	console.log('new connection: ' + socket.id);
	
	socket.on('query', runQuery);

	function runQuery(query){
		socket.emit('data');
		var spawn = require('child_process').spawn;
    		var pythonProcess = spawn('python3', ["test.py", query]);

		pythonProcess.stdout.on('data', function (data){
			console.log(data.toString());
			socket.emit('data', data.toString());
		});
		
	}
}
