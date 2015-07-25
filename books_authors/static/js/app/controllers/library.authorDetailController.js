'use strict';

library.controller('authorDetailCtrl', function ($scope, $http, $routeParams) {
    $scope.author = {};

    $http
        .get('/api/authors/' + $routeParams.id + '/?format=json')
        .success(function (out_data) {
            $scope.author = out_data;
        });
});
