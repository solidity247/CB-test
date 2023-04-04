let user_id = "qsHDeeBYv4hOZlhDLIoF"



document.addEventListener('DOMContentLoaded', function () {
    fetch('/carbon-footprint/qsHDeeBYv4hOZlhDLIoF')
        .then(response =>  response.json())
        .then(data => {
            console.log( data.success )
            if (data.success) {
                const carbonFootprintValue = document.getElementById('carbon-footprint-value');
                carbonFootprintValue.textContent = `Carbon Footprint: ${data.carbonFootprint}`;
            } else {
                alert('Error fetching carbon footprint: ' + data.error);
                
             }
        })
        .catch(error => {
            
            alert('Error fetching carbon footprint: ' + error);
        });
});
