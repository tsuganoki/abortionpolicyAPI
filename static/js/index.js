  "use strict";
    console.log("index.js");

  $(document).ready(function() {
    console.log("document ready");
  })

  function getInfo() {
    //https://swapi.co/api/planets/1/
    $.get('https://swapi.co/api/planets/1/', displayTatooine)
    console.log("getInfo run")

  }
  function displayTatooine(results) {
    // console.log(results['climate'])
    $('#climate').html(results['climate'])
    $('#terrain').html(results['terrain'])
    $('#population').html(results['population'])

  }


  $('#getInfo').on('click',getInfo)


var rp = require('request-promise');

var apiKey = open("token.txt").read()
console.log(apiKey)

// Count the number of states that require parental consent for minors
rp({
    uri: 'http://api.abortionpolicyapi.com/v1/minors/states',
    method: 'GET',
    headers: { 'token': apiKey },
    json: true
}).then(function success(response) {
    if (response) {
        var states = Object.keys(response);
        var count = states.reduce((count, state) => {
            return count + (response[state].parental_consent_required == true); 
        }, 0);

        console.log(`Number of states that require parental consent: ${count}`);
    }
}).catch(function error(response) {
    console.log(response.error);
});