'use strict';

library.controller('booksCtrl', function ($scope, $http) {

    $scope.books = [];

    // GET list of available books
    $http
        .get('/api/books/?format=json')
        .success(function (out_data) {
            for (var i = 0; i < out_data.length; i++) {
                $scope.books.push(out_data[i]);
            }
        });
});