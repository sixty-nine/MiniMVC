 $(document).ready(function () {
    
    setTimeout( 'window.location.reload()', 30000 );
    
    function ajax(url) {
         $.ajax({
            url: url,
            success: function(data) {
                window.location.reload();
            }
        });
    }
    
    $('.torrent_start').click(function () {
        ajax('/torrent/start/' + $(this).attr('id'));
    });

    $('.torrent_stop').click(function () {
        ajax('/torrent/stop/' + $(this).attr('id'));
    });

    $('#start_all_torrents').click(function () {
        ajax('/torrent/start/all');
    });

    $('#stop_all_torrents').click(function () {
        ajax('/torrent/stop/all');
    });

});
