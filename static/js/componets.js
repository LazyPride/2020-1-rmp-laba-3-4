class Component {
    constructor(control) {
        this.control = control;
        this.room_name = control.dataset["room_name"];
        this.id = control.dataset["id"];
        this.var_name = control.dataset["var_name"];
        if (control.type == "checkbox") {
            this.var_val = control.checked ? 1 : 0;
        }
        else if (control.type == "range") {
            this.var_val = control.value;
        }
        
        // Event handler. Gets value and notify connection
        this.control.onchange = (event) => {
            if (event.target.type == "checkbox") {
                this.var_val = event.target.checked ? 1 : 0;
                
            }
            else if (event.target.type == "range") {
                this.var_val = event.target.value;
            }
            let json_file = JSON.stringify(this);
            connectionNotify(json_file);
        };
    }
    
}

var ComponentCollection = [];

function initializeComponets() {
    var controls = document.getElementsByTagName("input");
    for (let control of controls) {
        component = new Component(control);
        // Push Component
        ComponentCollection.push(component);
    }
}


document.addEventListener('DOMContentLoaded', function(){ 
    initializeComponets();
});