(function (exports) {
    "use strict";

    function initMap(type_trajet) {

        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 6,
            center: { lat: 46.617578, lng: 2.506741 },
            mapTypeId: 'terrain'
        });

        $.ajax({
            type: "GET",
            url: "/get_coordonnees",
            success: callbackFunc,
            data: {
                type_trajet: String(type_trajet)
            },
        });

        var flightPlanCoordinates = [];

        function callbackFunc(response) {

            console.log(response);

            let b_duree = $('#duree')
            b_duree.empty();
            b_duree.append("<p>" + response.duree + " secondes</p>");

            let b_ecologique = $('#pollution');
            b_ecologique.empty();
            b_ecologique.append("<p>" + response.pollution + "gEc</p>");

            flightPlanCoordinates = response.coord;

            var flightPath = new google.maps.Polyline({
                path: flightPlanCoordinates,
                geodesic: true,
                strokeColor: '#ef982e',
                strokeOpacity: 1.0,
                strokeWeight: 2
            });
    
            flightPath.setMap(map);
        }
    }

    exports.initMap = initMap;
})((this.window = this.window || {}));


