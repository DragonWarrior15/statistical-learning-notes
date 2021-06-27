function set_content_height(){
    // sm breakpoint
    // $('body').css('height', $(window).height());
    if($(window).width() >= 768){
        $('body').css('overflow', 'hidden');
        var content_height = $(window).height() - $('#default_header').height() - $('#default_footer').height();
        $('#default_content').css('height', content_height);
        $('#default_content').css('overflow', 'auto');
        $('#sidebar').css('height', content_height);
        $('#sidebar').css('overflow', 'auto');
    }else{
        $('body').css('overflow', 'visible');
        $('#default_content').css('overflow', 'visible');
        $('#sidebar').css('overflow', 'visible');
    }
};

$(document).ready( function(){
    if($(window).width() < 768){
        $('#sidebar').collapse();
    };
    set_content_height();
});
$(window).resize(set_content_height());

$('#sidebar').on('shown.bs.collapse', function() {
    if($(window).width() >= 768){
        var content_height = $(window).height() - $('#default_header').height() - $('#default_footer').height();
        $('#sidebar').css('height', content_height);
        $('#sidebar').css('overflow', 'auto');
    }else{
        $('#sidebar').css('overflow', 'visible');
    }
});
