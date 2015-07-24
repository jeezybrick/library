'use strict';

library.controller('authorsCtrl', function ($scope, $http) {

    // Initialization
    $scope.authors = [];

    // GET list of available authors
    $http
        .get('/api/authors/?format=json')
        .success(function (data) {
            for (var i = 0; i < data.length; i++) {
                $scope.authors.push(data[i]);
            }
        });
});
