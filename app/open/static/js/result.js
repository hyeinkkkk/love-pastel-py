openApp.controller('ResultControllor', function($scope,$http,$location,playerTypeStorage, $routeParams)
{
    playerId = $routeParams['playerId']
    if(playerTypeStorage.get() == undefined) {
        $location.path("/list/"+playerId)
    }
    $scope.type = playerTypeStorage.get();
    $scope.nextPage = function(){
        console.log("enter");
        $location.path("/thanks");
    }
});
