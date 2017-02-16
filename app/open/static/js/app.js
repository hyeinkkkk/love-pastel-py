var openApp = angular.module('openApp',['ngRoute','ngMaterial','ngSanitize']);

openApp.config([
    "$routeProvider", function($routeProvider) {
        $routeProvider.when('/intro', {
            controller: 'IntroControllor',
            templateUrl: 'static/html/intro.html'
        }).when('/survey', {
            controller: 'SurveyControllor',
            templateUrl: 'static/html/survey.html'
        }).when('/list/:playerId', {
            controller: 'ListControllor',
            templateUrl: 'static/html/list.html'
        }).when('/priority/:playerId', {
            controller: 'PriorityControllor',
            templateUrl: 'static/html/priority.html'
        }).when('/result/:playerId', {
            controller: 'ResultControllor',
            templateUrl: 'static/html/result.html'
        }).when('/thanks', {
            controller: 'ThanksControllor',
            templateUrl: 'static/html/thanks.html'
        })
        .otherwise({
            redirectTo: "/intro"
        });
    }
]);

openApp.filter("newLineByComma", function($filter) {
 return function(data) {
   if (!data) return data;
   return data.replace(',', '<br>');
//   return data.replace(/\n\r?/g, '<br />');
 };
});

//openApp.config(function($mdThemingProvider) {
//    $mdThemingProvider.theme('default')
//      .primaryPalette('red', {
//        'default': 'A100', // by default use shade 400 from the pink palette for primary intentions
//        'hue-1': '50', // use shade 100 for the <code>md-hue-1</code> class
//        'hue-2': '600', // use shade 600 for the <code>md-hue-2</code> class
//        'hue-3': 'A100' // use shade A100 for the <code>md-hue-3</code> class
//    })
//      // If you specify less than all of the keys, it will inherit from the
//      // default shades
//      .accentPalette('purple', {
//        'default': '200' // use shade 200 for default, and keep all other shades the same
//      });
//});


openApp.factory('dataStorage', function() {
     var savedData = undefined
     function set(data) {
       savedData = data;
     }
     function get() {
      return savedData;
     }

     return {
      set: set,
      get: get
     }

});

openApp.factory('playerTypeStorage', function() {
     var savedData = undefined
     function set(data) {
       savedData = data;
     }
     function get() {
      return savedData;
     }

     return {
      set: set,
      get: get
     }

});

