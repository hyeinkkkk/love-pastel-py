openApp.controller('ThanksControllor', function($scope,$http,$location)
{
    $scope.enter = function(){
        console.log("enter");
        $location.path("/survey");
    }
});
