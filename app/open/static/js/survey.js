openApp.controller('SurveyControllor', function($scope,$http,$location)
{
    $scope.age = 0;
    $scope.gender = "";
    $scope.language = "ko";

    $scope.enter = function(){
        if($scope.age==0 || $scope.gender==""){
            return;
        }

        $http.get("/add-player/"+$scope.age + "/"+$scope.gender)
        .then(function(response){
            console.log("response? ",response.data.player_id);
            $location.path("/list/"+response.data.player_id);
        });

    }
});
