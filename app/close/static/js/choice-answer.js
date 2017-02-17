openApp.controller('ChoiceAnswerControllor', function($scope,$http,$location,dataStorage)
{
    $scope.myChoiceList = new Array();
    currentIndex = 0;
    function getChoices(){
        $http.get("/choices")
        .then(function(response){
            $scope.choiceList = response.data.choice_list;
            $scope.currentChoice = $scope.choiceList[currentIndex]
            console.log("response? ",response.data);
        });
    }

    getChoices();

    $scope.clickAnswer = function(choice, type){
        answer = {};
        answer.point = choice['type_'+type+'_point'];
        answer.type = type;
        answer.text = choice['type_'+type];
        answer.choice_id = choice.id;

        $scope.myChoiceList.push(answer);
        $scope.currentChoice = $scope.choiceList[++currentIndex];
        console.log("enter " , $scope.myChoiceList);

        if($scope.choiceList.length == currentIndex){
            temperature = 36.5;
            angular.forEach($scope.myChoiceList , function(choice) {
                temperature += choice.point;
            });

            console.log("temperature?? ",parseFloat(temperature).toFixed(1))
            data = {choice_list : $scope.myChoiceList, temperature: temperature}
            dataStorage.set(data)
            $location.path("/result");
        }

    }

    $scope.previous = function(){
        $scope.myChoiceList.pop();
        $scope.currentChoice = $scope.choiceList[--currentIndex];
    }
});
