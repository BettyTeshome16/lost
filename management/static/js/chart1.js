var ctx = document.getElementById('lineChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        datasets: [{
            label: 'Lost Items ',
            data: [50, 20, 3, 30, 100, 150, 50, 55, 80, 140, 45, 10],
            
            backgroundColor: [
                'rgba(85,85,85, 1)'
                
                

            ],
            
            borderColor: 'rgb(41, 155, 99)',

            borderWidth: 1
        }]
        
    },
    
    options: {
        responsive: true
    }
});