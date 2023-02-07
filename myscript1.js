/*<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script> */



$.ajax({
    url: 'http://your-api-endpoint.com/videos',
    method: 'GET'
  })
    .done(function(data) {
      console.log(data);
      // use the data however you like here
    })
    .fail(function(error) {
      console.error('There was a problem with the fetch operation:', error);
    });
  