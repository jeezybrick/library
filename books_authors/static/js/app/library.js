'use strict';

var library = angular.module('libraryApp', ['ngRoute']);

library
    .config(function ($httpProvider) {
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
    });

library.config(function ($routeProvider) {
    $routeProvider.when('/authors', {
        templateUrl: '/static/templates/library/authors.html'
    });
    $routeProvider.when('/books', {
        templateUrl: '/static/templates/library/books.html'
    });
    $routeProvider.when('/genres', {
        templateUrl: '/static/templates/library/genres.html'
    })

});
