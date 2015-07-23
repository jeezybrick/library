'use strict';

library.controller('authorsCtrl', function ($scope, $http) {
    $scope.authors = [];
    $scope.reset_form = function () {
        $scope.name = '';
        $scope.slug = '';
    };
    $scope.addAuthor = function () {
        var in_data = {
            name: $scope.name,
            slug: $scope.slug
        };

        $http
            .post('/api/authors/?format=json', in_data)
            .success(function (out_data) {
                $scope.authors.push(out_data);
                $scope.reset_form();
            });
    };
    $scope.deleteAuthor = function (index, element, id) {
        $http
            .delete('/api/authors/' + id + '/')
            .success(function () {
                $scope.authors.splice(index, 1);
            });
    };

    $scope.reset_form();

    $http
        .get('/api/authors/?format=json')
        .success(function (data) {
            for (var i = 0; i < data.length; i++) {
                $scope.authors.push(data[i]);
            }
        });
});
