openApp.controller('ResultControllor', function($scope,$http,$location,dataStorage)
{
    data = dataStorage.get();
    if(data== undefined){
        $location.path("/choice-answer");
        return;
    }
    function getMyTemperature(){

        postData = data
        $http.post("/temperatures", postData)
        .then(function(response){
            $scope.myTemperature = response.data.my_temperature;
            $scope.myResult = response.data.my_result;
        });
    }

    getMyTemperature();

    $scope.nextPage = function(){
        $location.path("/thanks");
    }
});
