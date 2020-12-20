class Status {
    constructor(status) {
        this.status = status.getElementsByTagName("span")[0];
        this.room_name = status.dataset["room_name"];
        this.id = status.dataset["id"];
        this.var_name = status.dataset["var_name"];
    }
    
    tryUpdate(id, varName, value) {
        if (this.id != id || this.var_name != varName) return false;
        
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

function tryUpdateStatuses(id, varName, value) {
    let hasUpdated = false;
    for (let status of StatusCollection) {
        if (status.tryUpdate(id, varName, value)) {
            hasUpdated = true;
            console.log("[Status]: " + id + ": The " + varName + " is " + value);
        }
    }
    return hasUpdated;
}
document.addEventListener('DOMContentLoaded', function(){ 
    initializeStatuses();
});