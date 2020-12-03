class Component {
    constructor(control) {
        console.log(control.dataset);
        this.control = control;
        this.roomName = control.dataset["roomname"];
        this.varName = control.dataset["varname"];
        if (control.type == "checkbox") {
            this.varValue = control.checked;
        }
        else if (control.type == "range") {
            this.varValue = control.value;
        }
        
        // Event handler. Gets value and notify connection
        this.control.onchange = (event) => {
            if (event.target.type == "checkbox") {
                this.varValue = event.target.checked;
            }
            else if (event.target.type == "range") {
                this.varValue = event.target.value;
            }
            json = JSON.stringify(this);
            connectionNotify(json);
        };
    }
    
}

var ComponentCollection = [];

function initializeComponets() {
    var controls = document.getElementsByTagName("input");
    console.log(controls);
    for (let control of controls) {
        component = new Component(control);
        // Push Component
        ComponentCollection.push(component);
    }
    console.log(ComponentCollection);
}


document.addEventListener('DOMContentLoaded', function(){ 
    initializeComponets();
});