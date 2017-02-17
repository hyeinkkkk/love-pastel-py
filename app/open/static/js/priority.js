openApp.controller('PriorityControllor', function($scope,$http,$location,$routeParams,dataStorage,$filter,playerTypeStorage)
{

    $scope.maxCount = 3;

    playerId = $routeParams['playerId'];

    resetSongs = function(){
        $scope.priorityArr = new Array();
        $scope.songs = dataStorage.get();
        if($scope.songs == undefined) {
            console.log("songs?? ")
            $location.path("/list/"+playerId)
        }
        angular.forEach( $scope.songs , function(song) {
            song.priorityCheck = false;
            song.priority = 0;
        });


    }

    resetSongs();

    $scope.selectSongs = function(item,event){
        if(!item.priorityCheck){
            item.priorityCheck = true;
            $scope.priorityArr.push(item);
            item.priority = $scope.priorityArr.length;
        }else if(item.priorityCheck && item.priority == $scope.priorityArr.length){
            item.priorityCheck = false;
            item.priority = 0;
            $scope.priorityArr.pop();

        }
        if($scope.priorityArr.length == $scope.maxCount){
            console.log("d?F?F?");
        }
        console.log("priorityArr ",$scope.priorityArr.length);
    };

    $scope.nextPage = function(){
        typeList = new Array();

        angular.forEach( $scope.priorityArr , function(song) {
            exist = false

            for(i=0; i<typeList.length; i++){
                console.log("type?? ",typeList[i])
                if(typeList[i].id == song.type_id){
                    exist = true
                    if(song.priority < typeList[i].priority){
                        typeList[i].priority = song.priority;
                    }
                    typeList[i].count ++;
                }
            }
            if(!exist){
                typeList.push({id: song.type_id, count: 1, priority:song.priority})
            }
        });

        playerType = $filter('orderBy')(typeList,'count',-1)[0]
        if(playerType.count == 1){
            playerType = $filter('orderBy')(typeList,'priority')[0]
        }

        $http({
          url: "/submit-vote",
          method: "POST",
          headers: { 'Content-Type': 'application/json' },
          data: JSON.stringify({player_id: playerId, vote: $scope.priorityArr, player_type: playerType.id})
        }).then(function(response) {
            console.log("response?? ", response)
            playerTypeStorage.set(response.data.player_type);
            $location.path("/result/"+playerId);
        });
//        $location.path("/result");
    }

});
