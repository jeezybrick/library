'use strict';

library.controller('booksCtrl', function ($scope, $http) {

    // Initialization
    $scope.books = [];
    //$scope.title = '';
    //$scope.author = '';
    //$scope.annotation = '';
    //$scope.genre = [];
    //$scope.slug = '';

    // GET list of available books
    $http
        .get('/api/books/?format=json')
        .success(function (out_data) {
            for (var i = 0; i < out_data.length; i++) {
                $scope.books.push(out_data[i]);
                console.log(out_data[i]);
            }
        });
});