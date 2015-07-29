'use strict';

library.controller('bookDetailCtrl', function ($scope, $http, $routeParams) {
    $scope.book = {};

    $http
        .get('/api/books/' + $routeParams.id + '/?format=json')
        .success(function (out_data) {
            console.log(out_data);
            $scope.book = out_data;
        });
});
