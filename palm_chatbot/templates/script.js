// Get the response element
var responseElement = document.getElementById("response");

// Listen for form submit events
document.querySelector("form").addEventListener("submit", function(event) {
  // Prevent the default form submit behavior
  event.preventDefault();

  // Get the user's input
  var user_input = document.querySelector("input[name='user_input']").value;

  // Make a POST request to the server to get the response
  fetch("/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ user_input: user_input })
  }).then(function(response) {
    // Get the response JSON
    return response.json();
  }).then(function(data) {
    // Set the response element's text to the response from the server
    responseElement.textContent = data.response;
  });
});
