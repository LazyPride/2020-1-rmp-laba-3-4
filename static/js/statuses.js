class Status {
    constructor(status) {
        this.status = status.getElementsByTagName("span")[0];
        this.roomName = status.dataset["roomname"];
        this.varName = status.dataset["varname"];
    }
    
    tryUpdate(roomName, varName, value) {
        if (this.roomName != roomName || this.varName != varName) return false;
        
        this.status.innerHTML = value;
        return true;
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
}

function tryUpdateStatuses(roomName, varName, value) {
    let hasUpdated = false;
    for (let status of StatusCollection) {
        if (status.tryUpdate(roomName, varName, value)) hasUpdated = true;
    }
    return hasUpdated;
}

document.addEventListener('DOMContentLoaded', function(){ 
    initializeStatuses();
});