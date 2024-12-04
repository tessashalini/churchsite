$(document).ready(function() {
    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        editable: false,
        events: '/path-to-fetch-events/'  // Replace with your actual path
    });
});

function showForm() {
    document.querySelectorAll('.event-form').forEach(form => {
        form.style.display = 'none';
    });
    const selectedEvent = document.getElementById('event-type').value;
    if (selectedEvent) {
        document.getElementById(selectedEvent + '-form').style.display = 'block';
    }
}

