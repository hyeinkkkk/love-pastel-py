openApp.controller('ThanksControllor', function($scope,$http,$location)
{
    function getState(){
        $http.get("/concert/state")
        .then(function(response){
            console.log("ssS??? ")
            if(response.data.state == "close"){
                window.location = "http://bit.ly/love-pastel";
            }

//            $location.url("/close");
        });
    }

    getState();
    $scope.enter = function(){

        console.log("enter");
        $location.path("/survey");
    }
});
