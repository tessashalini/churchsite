document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/booked-events/')
        .then(response => response.json())
        .then(data => {
            const bookedDates = data.map(event => event.date);
            const bookedTimes = data.map(event => event.time);

            const dateInput = document.getElementById('date');
            const timeInput = document.getElementById('time');

            dateInput.addEventListener('change', function() {
                if (bookedDates.includes(this.value)) {
                    alert('This date is already booked.');
                    this.value = '';
                }
            });

            timeInput.addEventListener('change', function() {
                if (bookedTimes.includes(this.value)) {
                    alert('This time is already booked.');
                    this.value = '';
                }
            });
        });
});
