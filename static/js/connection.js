console.log("[Socket]: Initialization...");
var socket = io();
console.log("[Socket]: Created.");
var chart = new MyChart();

socket.on('connect', function() {
    console.log("[Socket]: Connected.");
    socket.emit('sync');
    console.log("[Socket]: Start synchronizing.");

});

socket.on('sync', function(json) {
    console.log("[Socket]: synchronizing...");
    console.log(json);
    for (let room of json['rooms']) {
        for (let component of room['components']) {
            tryUpdateStatuses(component["id"], "is_on", component["is_on"]);
            tryUpdateStatuses(component["id"], "now", component["now"]);
            tryUpdateStatuses(component["id"], "min", component["min"]);
            tryUpdateStatuses(component["id"], "max", component["max"]);
        }
    }
    console.log("[Socket]: Synchronizing completed.");

});

socket.on('update-confirm', function(json) {
    console.log("[Socket]: Receive update-confirm from the server.");
    let jsonObj = JSON.parse(json);
    tryUpdateStatuses(jsonObj['id'], jsonObj['var_name'], jsonObj['var_val']);
});

socket.on('update', function(json) {
    console.log("[Socket]: Receive update from the server");
    let jsonObj = JSON.parse(json);
    tryUpdateStatuses(jsonObj['id'], jsonObj['var_name'], jsonObj['var_val']);
    
    if (jsonObj['id'] == 'heater_1' && jsonObj['var_name'] == 'now') {
        chart.add(jsonObj['var_val']);
    }
    
    socket.emit('update-confirm', json);
    console.log("[Socket]: Emit update-confirm to the server");
});

function connectionNotify(json) {
    socket.emit('update', json);
    console.log("[Socket]: Emit update to the server");

}