document.addEventListener('DOMContentLoaded', function() {
  const jobIdDropdown = document.getElementById('jobs');
  const applicationIdDropdown = document.getElementById('application');

  jobIdDropdown.addEventListener('change', function() {
    const selectedJobId = this.value;

    // Send an AJAX request to your Python backend
    const xhr = new XMLHttpRequest();
    xhr.open('GET', `/get_applications/${selectedJobId}`);
    xhr.onload = function() {
      if (xhr.status >= 200 && xhr.status < 300) {
        const applications = JSON.parse(xhr.response); 

        // Clear existing options in the second dropdown
        applicationIdDropdown.innerHTML = '';

        // Add new options based on fetched data
        applications.forEach(application => {
          const option = document.createElement('option');
          option.value = application.id;
          option.text = application.Application; 
          applicationIdDropdown.add(option);
        });
      } else {
        console.error('Error fetching applications:', xhr.status, xhr.statusText);
      }
    };
    xhr.send();
  });
});

