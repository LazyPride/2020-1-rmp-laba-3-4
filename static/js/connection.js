console.log("[Socket]: Initialization...");
var socket = io();
console.log("[Socket]: Created.");
socket.on('connect', function() {
    socket.emit('my event', {data: 'I\'m connected!'});
    console.log("[Socket]: Connected.");
});