class Status {
    constructor(status) {
        this.status = status.getElementsByTagName("span")[0];
        this.roomName = status.dataset["roomname"];
        this.varName = status.dataset["varname"];
    }
    
    tryUpdate(roomName, varName, value) {
        if (this.roomName != roomName || this.varName != varName) return
        
        this.status.innerHTML = value;
    }
}

var StatusCollection = [];

function initializeStatuses() {
    var statuses = document.querySelectorAll(".room-status-component");
    for (let status of statuses) {
        status = new Status(status);
        // Push Status
        StatusCollection.push(status);
    }
    console.log(StatusCollection);
}

function tryUpdateStatuses(roomName, varName, value) {
    StatusCollection.forEach(status => {
        status.tryUpdate(roomName, varName, value);
    });
}

document.addEventListener('DOMContentLoaded', function(){ 
    initializeStatuses();
});