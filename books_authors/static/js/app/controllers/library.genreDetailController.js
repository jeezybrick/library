'use strict';

library.controller('genreDetailCtrl', function ($scope, $http, $routeParams) {
    $scope.genre = {};

    $http
        .get('/api/genres/' + $routeParams.id + '/?format=json')
        .success(function (out_data) {
            $scope.genre = out_data;
        });
});
