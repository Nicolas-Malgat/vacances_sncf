<!DOCTYPE html>
<html>

<head>
    <title>Map</title>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=default"></script>
    <script src="https://maps.googleapis.com/maps/api/js?key=&callback=initMap&libraries=drawing&v=weekly"
        defer></script>
    <!-- jsFiddle will insert css and js -->

    <script src="/javascript/draw.js"></script>
    <script src="/javascript/top_bar.js"></script>
</head>

<body>

    % include('top_bar.html')

    <div id="map"></div>

    <link href="/css/top_bar.css" rel="stylesheet">
    <style>
        /* Always set the map height explicitly to define the size of the div
       * element that contains the map. */
        #map {
            height: 100%;
        }

        /* Optional: Makes the sample page fill the window. */
        html,
        body {
            overflow-y: hidden;
            height: 100%;
            margin: 0;
            padding: 0;
        }
    </style>
</body>

</html>