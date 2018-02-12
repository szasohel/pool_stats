$(document).ready(function() {
    "use strict"

    var player1 = $(".select-player1");
    var player2 = $(".select-player2");
    var start_btn = $(".start-game-btn");
    var play_btn = $(".play-game-btn");
    var create_player = $(".create-player-btn")

    start_btn.click(function(event) {
        if (player1.val() === player2.val()) {
            event.preventDefault();
            alert("There is no fun playing alone\n" +
                "Please enter two different players' name");
        }
    });


    play_btn.click(function(event) {
        var winner = $("input[name=player]:checked").val();
        if (winner) {
        	event.preventDefault();
            $(".greet-text").html("<h1>Congratulations " +
                winner + "!</h1>").slideDown(1000);
            $(".greet-text").delay(2000).slideUp(1000);
        }
        else if(!winner){
        	event.preventDefault();
        	alert("Please select a winner")
        }

    });

    create_player.click(function(event) {
        var player = $("#create-player").val()
        if (!player) {
        	event.preventDefault();
            alert("Please enter a name")
        }

    });

}($));