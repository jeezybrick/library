'use strict';

library.controller('authorsCtrl', function ($scope, $http, $routeParams) {

    // Initialization
    $scope.authors = [];

    // Pagination
    $scope.pages = [];
    $scope.curPage = parseInt($routeParams.page) || 1;
    $scope.nextPage = $scope.curPage + 1 || null;
    $scope.previousPage = $scope.curPage - 1 || null;
    $scope.GETUrl = '/api/authors/?format=json';

    if ($routeParams.page) {
        $scope.GETUrl += '&page=' + $scope.curPage;
    }

    // GET list of available authors
    $http
        .get($scope.GETUrl)
        .success(function (data) {
            // Is previous (and next) page exists?
            $scope.previousExist = !!data.previous;
            $scope.nextExist = !!data.next;

            $scope.previousAPIUrl = data.previous;
            $scope.nextAPIUrl = data.next;

            if (data.count > 15) {
                $scope.showPaginator = true;
                for (var i = 1; i <= data.last; i++) {
                    $scope.pages.push(i);
                }
            } else {
                $scope.showPaginator = false;
            }

            for (var i = 0; i < data.results.length; i++) {
                $scope.authors.push(data.results[i]);
            }
        });
});
