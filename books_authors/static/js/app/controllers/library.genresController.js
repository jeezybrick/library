'use strict';

library.controller('genresCtrl', function ($scope, $http) {
    $scope.genres = [];

    $http
        .get('/api/genres/?format=json')
        .success(function (out_data) {
            for (var i = 0; i < out_data.length; i++) {
                $scope.genres.push(out_data[i]);
            }
        });
});
