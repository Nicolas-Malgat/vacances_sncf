(function(exports) {
    "use strict";
  
    // This example requires the Drawing library. Include the libraries=drawing
    // parameter when you first load the API. For example:
    // <script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=drawing">
    function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 7,
      center: {lat: 49.57501319148936, lng: 3.61810441489362},
      mapTypeId: 'terrain'
    });
  
    var flightPlanCoordinates = [
      {lat: 46.2051192, lng: 5.2250324},
      {lat: 49.57501319148936, lng: 3.61810441489362},
      {lat: 49.41994084745765, lng: 3.68123322033898},
      {lat: 46.5660526, lng: 3.3331703}
    ];
    var flightPath = new google.maps.Polyline({
      path: flightPlanCoordinates,
      geodesic: true,
      strokeColor: '#FF0000',
      strokeOpacity: 1.0,
      strokeWeight: 2
    });
  
    flightPath.setMap(map);
  }
  
    exports.initMap = initMap;
  })((this.window = this.window || {}));