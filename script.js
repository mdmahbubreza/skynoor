document.getElementById('search-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const origin = document.getElementById('origin').value;
    const destination = document.getElementById('destination').value;
    const departureDate = document.getElementById('departure-date').value;

    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ origin, destination, departureDate })
    })
    .then(response => response.json())
    .then(data => {
        const resultsDiv = document.getElementById('results');
        resultsDiv.innerHTML = '<h2>Search Results</h2>';
        if (data.flights.length > 0) {
            data.flights.forEach(flight => {
                resultsDiv.innerHTML += `<p>${flight.airline}: ${flight.price}</p>`;
            });
        } else {
            resultsDiv.innerHTML += '<p>No flights found.</p>';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('results').innerHTML = '<p>Error fetching flight data. Please try again later.</p>';
    });
});
