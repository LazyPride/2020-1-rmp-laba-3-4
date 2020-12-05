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
    for (let obj of json) {
        tryUpdateStatuses(obj["roomName"], "lightState", obj["lightState"]);
        tryUpdateStatuses(obj["roomName"], "lightBrightness", obj["lightBrightness"]);
        tryUpdateStatuses(obj["roomName"], "temperature", obj["temperature"]);
    }
    console.log("[Socket]: Synchronizing completed.");

});

socket.on('update-confirm', function(json) {

    console.log("[Socket]: Receive update-confirm from the server.");
    let jsonObj = JSON.parse(json)
    tryUpdateStatuses(jsonObj['roomName'], jsonObj['varName'], jsonObj['varValue'])
});

socket.on('update', function(json) {

    console.log("[Socket]: Receive update from the server");
    let jsonObj = JSON.parse(json)
    tryUpdateStatuses(jsonObj['roomName'], jsonObj['varName'], jsonObj['varValue']);
    socket.emit('update-confirm', json);
    console.log("[Socket]: Emit update-confirm to the server");
});

function connectionNotify(json) {
    socket.emit('update', json);
    console.log("[Socket]: Emit update to the server");

}