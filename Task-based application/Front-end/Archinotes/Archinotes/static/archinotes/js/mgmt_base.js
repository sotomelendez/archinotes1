function switchMenu(){
    if($('#management_menu').hasClass('nav')){
        var editor = $('#editor_menu')
        editor.addClass($('#management_menu').attr('class'))
        $('#editor_menu li a').each(function() {
            $(this).addClass('btn btn-default');
        });
        var management = $('#management_menu')
        management.prop('class', null)
        $('#management_menu li a').each(function() {
            $(this).prop('class', null);
        });
        $('#top_menu').empty()
        $('#top_menu').append(editor)
        $('#sidr').empty()
        $('#sidr').append(management)
    }
    else if($('#editor_menu').hasClass('nav')){
        var management = $('#management_menu')
        management.addClass($('#editor_menu').attr('class'))
        $('#management_menu li a').each(function() {
            $(this).addClass('btn btn-default');
        });
        var editor = $('#editor_menu')
        editor.prop('class', null)
        $('#editor_menu li a').each(function() {
            $(this).prop('class', null);
        });
        $('#top_menu').empty()
        $('#top_menu').append(management)
        $('#sidr').empty()
        $('#sidr').append(editor)
    }
};