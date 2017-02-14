openApp.controller('IntroControllor', function($scope,$http,$location)
{
    $scope.enter = function(){
        console.log("enter");
        $location.path("/survey");
    }
});
