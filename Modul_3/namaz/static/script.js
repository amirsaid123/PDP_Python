<script>
    function fetchPrayerTimes(cityId) {
        fetch(`/city/${cityId}/times`)
            .then(response => response.json())
            .then(data => {
                let tableBody = document.getElementById('times-table-body');
                tableBody.innerHTML = '';  // Clear existing rows
                data.forEach(time => {
                    let row = document.createElement('tr');
                    row.innerHTML = `<td>${time.namoz}</td><td>${time.time}</td>`;
                    tableBody.appendChild(row);
                });
            })
    }
</script>
