console.log("[Socket]: Initialization...");
var socket = io();
console.log("[Socket]: Created.");

socket.on('connect', function() {
    console.log("[Socket]: Connected.");
    socket.emit('sync');
    console.log("[Socket]: Start synchronizing.");

});

socket.on('sync', function(json) {
    console.log("[Socket]: synchronizing...");
    // TODO: Synchronize variables OR make it all in the template
    console.log(json);
});

socket.on('update-confirm', function(json) {

    console.log("[Socket]: Value updated on client confirmed.");
    console.log(json);
});

socket.on('update', function(json) {

    console.log("[Socket]: Value updated on server.");
    console.log(json);
    socket.emit('update-confirm', json);
});

function connectionNotify(json) {
    socket.emit('update', json)
}