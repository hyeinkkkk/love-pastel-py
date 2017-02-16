openApp.controller('ResultControllor', function($scope,$http,$location,dataStorage)
{
    myTemperature = dataStorage.get();
    if(myTemperature == undefined){
        $scope.myTemperature = 141.5;
        $scope.myResult = {description: "태양처럼 한곁같이 뜨거울 사랑의 온기를 지니셨군요. 역시 사랑에는 계산이 없어야 하죠."};
//        $location.path("/choice-answer");
        return;
    }
    function getMyTemperature(){
        postData = myTemperature
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
