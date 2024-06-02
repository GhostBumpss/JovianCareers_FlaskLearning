  document.addEventListener('DOMContentLoaded', function() {
    const loginForm = document.getElementById('create_login');
  
    loginForm.addEventListener('submit', function(event) {
      event.preventDefault(); // Preventing default form submission
  
      const loginFormdata = new FormData(loginForm); // Get the form data
  
      const xhr = new XMLHttpRequest();
      xhr.open('POST', '/loginsubmit');
      xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
  
      xhr.onload = function() {
        if (xhr.status >= 200 && xhr.status < 300) {
          console.log('Login created successfully', xhr.responseText);
        } else {
          coonsole.log('Error creating login', xhr.status, xhr.statusText);
        };
      };
  
      const formData = {};
      loginFormdata.forEach((value, key) => {
        formData[key] = value;
      });
  
      console.log(formData);
  
      xhr.send(JSON.stringify(formData));
    });
  });