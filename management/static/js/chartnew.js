Highcharts.chart('container', {
    chart: {
        type: 'pie',
        width: 800, // Set the width of the chart
        height: 400 // Set the height of the chart
    },
    title: {
        text: 'Lost Item Categories',
        align: 'left'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Lost Items',
        colorByPoint: true,
        data: [
            {
                name: 'Electronics',
                y: 25
            },
            {
                name: 'Jewelry',
                y: 15
            },
            {
                name: 'Clothing',
                y: 20
            },
            {
                name: 'Accessories',
                y: 10
            },
            {
                name: 'Documents',
                y: 5
            },
            {
                name: 'Other',
                y: 25
            }
        ]
    }]
});