'use strict';

angular.module('myApp.view1', ['ngRoute'])

.config(['$routeProvider', function($routeProvider) {
  $routeProvider.when('/view1', {
    templateUrl: 'view1/view1.html',
    controller: 'View1Ctrl'
  });
}])

.controller('View1Ctrl', ["$scope", "$http", "$timeout", function($scope, $http, $timeout) {
     $scope.at_least_one_question_loaded = false;
     $scope.answer_choice = {};
     $scope.alert_message = "";
     $scope.alert_additional_details = [];
     $scope.is_loading = false;
     $scope.staging = false;
     $scope.show_log = false;
     $scope.question_tests = [];

     $scope.host = ""
     $scope.port = ""

     $scope.all_question_statuses = []

     $scope.test = function(){
        $scope.is_loading = true;
        $http.post("/test", {host: $scope.host, port: $scope.port}).then(function(response){
            $scope.is_loading = false;
            $scope.alert_message = response.data.message;
            $scope.alert_type = "success"
        }, function(response){
            $scope.is_loading = false;
            $scope.alert_message = response.data.message;
            $scope.alert_type = "failure"
            console.error(response)
        })

     }

}]);