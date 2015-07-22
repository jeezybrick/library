'use strict';

library.controller('authorsCtrl', function ($scope, $http) {
    $scope.authors = [];
    $scope.reset = function () {
        $scope.formName = '';
        $scope.formSlug = '';
    };
    $scope.addAuthor = function () {
        $http
            .post('/api/authors/')
            .success(function (data) {
                console.log('YAY! ' + data);
            });
        console.log('Added!');
        $scope.authors.push({
            name: $scope.formName
        });
        $scope.reset();
    };

    $scope.reset();

    $http
        .get('/api/authors/')
        .success(function (data) {
            for (var i = 0; i < data.length; i++) {
                console.log(data[i]);
                $scope.authors.push(data[i]);
            }
        });
});
