openApp.controller('IntroControllor', function($scope,$http,$location)
{
    $scope.nextPage = function(){
        $location.path("/choice-answer");
    }
});
