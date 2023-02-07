/*npm install axios*/

import axios from 'axios';

axios.get('http://your-api-endpoint.com/videos')
  .then(response => {
    console.log(response.data);
    // use the data however you like here
  })
  .catch(error => {
    console.error('There was a problem with the fetch operation:', error);
  });
