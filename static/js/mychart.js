
class MyChart {
    constructor() {
        var canvas = document.getElementById("line-chart");
        canvas.width  = 800;
        canvas.height = 600;
        
        this.chart = new Chart(canvas.getContext('2d'), {
            type: 'line',
            data: {
                labels: [],
                datasets: [{
                    label: 'Temperature',
                    steppedLine: true,
                    data: [],
                    borderColor: "#00FF00",
                    fill: false,
                }]
            },
            options: {
                responsive: false,
                maintainAspectRatio: false,
                title: {
                    display: true,
                    text: 'Temperature',
                }
            }
        });
        this.indexNo = 0
        this.maxCount = 120
    }
    
    add(value) {
        if (this.indexNo >= this.maxCount) {
            this.chart.data.labels.shift();
            this.chart.data.datasets[0].data.shift();
        }
        
        this.chart.data.labels.push(this.indexNo++);
        this.chart.data.datasets[0].data.push(value)
        this.chart.update();
            
    }
}
   