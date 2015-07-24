'use strict';

var library = angular.module('libraryApp', ['ngRoute']);

library.config(function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

library.config(function ($routeProvider) {
    // List routers
    $routeProvider.when('/authors', {
        templateUrl: '/static/templates/library/authors.html'
    });
    $routeProvider.when('/books', {
        templateUrl: '/static/templates/library/books.html'
    });
    $routeProvider.when('/genres', {
        templateUrl: '/static/templates/library/genres.html'
    });

    // Detail routers
    $routeProvider.when('/authors/:id', {
        templateUrl: '/static/templates/library/author_detail.html'
    });
    $routeProvider.when('/books/:id', {
        templateUrl: '/static/templates/library/book_detail.html'
    });

});
