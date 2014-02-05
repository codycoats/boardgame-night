$( function() {

    $('#event-date').datepicker();

    //mark unplayable games
    games = $('.game').detach();
    var playable =[];
    var unplayable = [];
    numAttendees = $("#attendeeCount_badge").data('count')

    $.each(games, function(item, game){
        if (numAttendees > $(game).data('maxplayers')) {
            $(game).attr('data-playable', false);
            unplayable.push(game);
        }
        else if(numAttendees < $(game).data('minplayers')){
            $(game).attr('data-playable', false);
            unplayable.push(game);
        }
        else{
            playable.push(game);
        }
    });


    //separate lists
    console.log(playable);
    console.log(unplayable);

    $('#playable-list').append(playable);
    $('#unplayable-list').append(unplayable);
});

