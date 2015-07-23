'use strict';

library.controller('authorsCtrl', function ($scope, $http) {

    // Initialization
    $scope.authors = [];
    $scope.resetForm = function () {
        $scope.name = '';
        $scope.slug = '';
    };
    $scope.formEditState = false;
    $scope.currentlyEditAuthor = null;

    // Edit switcher
    $scope.toggleEditForm = function (state, author) {
        $scope.formEditState = state;
        $scope.currentlyEditAuthor = author;

        if (state === false) {
            $scope.resetForm();
        } else {
            $scope.name = author.name;
            $scope.slug = author.slug;
        }
    };

    // GET method
    $http
        .get('/api/authors/?format=json')
        .success(function (data) {
            for (var i = 0; i < data.length; i++) {
                $scope.authors.push(data[i]);
            }
        });

    // POST method
    $scope.addAuthor = function () {
        var in_data = {
            name: $scope.name,
            slug: $scope.slug
        };

        $http
            .post('/api/authors/?format=json', in_data)
            .success(function (out_data) {
                $scope.authors.push(out_data);
                $scope.resetForm();
            });
    };

    // DELETE method
    $scope.deleteAuthor = function (index, element) {
        $http
            .delete('/api/authors/' + element.id + '/')
            .success(function () {
                $scope.authors.splice(index, 1);
            });
    };

    // PUT method
    $scope.editAuthor = function () {
        console.log($scope.currentlyEditAuthor);
        var in_data = {
            name: $scope.name,
            slug: $scope.slug
        };
        console.log(in_data);
        console.log('----------------------');
        console.log('http://localhost:8000/api/authors/' + $scope.currentlyEditAuthor.id + '/?format=json');
        $http
            .put('/api/authors/' + $scope.currentlyEditAuthor.id + '/?format=json', in_data)
            .success(function (out_data) {
                console.log('success! ' + JSON.stringify(out_data));
            })
    };

    $scope.resetForm();
});
