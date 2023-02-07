fetch('http://your-api-endpoint.com/videos')
  .then(response => response.json())
  .then(data => {
    console.log(data);
    // use the data however you like here
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });
