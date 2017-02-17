openApp.controller('ListControllor', function($scope,$http,$location,$routeParams,dataStorage)
{
    $scope.selectedArr = new Array();
//    $scope.count = 0;
    $scope.maxCount = 3;
    playerId = $routeParams['playerId'];


    function getSongs(){
        $http.get("/songs")
        .then(function(response){
            $scope.songs = response.data.song_list;
            angular.forEach($scope.songs , function(song) {
                song.check = false;
            });
            console.log("response? ",response.data);
        });
    }


    getSongs();

    $scope.selectSongs = function(item,event){
        if($scope.selectedArr.length == $scope.maxCount && !item.check){
            return;
        }
        if(!item.check){
            item.check = true;
            $scope.selectedArr.push(item);
            // item.priority = $scope.selectedArr.length;
        }else{
            console.log("$scope.selectedArr.indexOf(item)",$scope.selectedArr.indexOf(item));
            $scope.selectedArr.splice($scope.selectedArr.indexOf(item),1);
            item.check = false;
        }

        if($scope.selectedArr.length == $scope.maxCount){
            dialogText = ""
            dataStorage.set($scope.selectedArr);
        }

        console.log("priorityArr ",$scope.selectedArr);
    };

    $scope.nextPage = function(){
        $location.path("/priority/"+playerId);
    }
});
