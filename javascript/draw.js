var flightPlanCoordinates = null;

$(document).ready(function () {
    console.log('Passage dans le script draw.js')
    $.ajax({
        type: "GET",
        url: "/get_coordonnees",
        success: callbackFunc,
    });

    (function(exports) {
        "use strict";
    
        var flightPath = new google.maps.Polyline({
            path: flightPlanCoordinates,
            geodesic: true,
            strokeColor: '#FF0000',
            strokeOpacity: 1.0,
            strokeWeight: 2
        });
    
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 7,
            center: { lat: 46.617578, lng: 2.506741 },
            mapTypeId: 'terrain'
        });
    
        flightPath.setMap(map);
        
        exports.initMap = initMap;
    })((this.window = this.window || {}));
})

function callbackFunc(response) {

    console.log(response);

    flightPlanCoordinates = response;
}

