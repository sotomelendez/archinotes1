$(document).ready(function() {
    $("#id_teams option:first").attr('selected','selected');
    $('#id_teams').trigger('change');
    $('.add_project').click(function() {
        var option_value = $('#id_teams').val();
        $('#id_team').val(option_value);
    });
});
$( "#id_teams" ).change(function () {
    var option_value = $('#id_teams').val();
    var url_value = $('#team_projects').val();
    $.ajax({
        dataType : 'json',
        url : url_value,
        type : 'GET',
        data : {'team':option_value},
        success : function(data) {
            var projects = data['projects'];
            $('#projects').empty();
            if(projects.length>0){
                for(i = 0; i < $(projects).length; i++){
                    var name = projects[i]['name']
                    var description = projects[i]['description'].replace(/ /g,"_")
                    var url = $('#proj_url').val().replace('name',name);
                    var content = $("<a href='"+url+"' id="+name+" data-toggle='tooltip' title="+description+" class='btn btn-default' style='margin:10px'><i class='fa fa-fighter-jet fa-4x'></i><p>"+name+"</p></a>");                   
                    $(content).tooltip();
                    $( "#projects" ).append($(content));
                }
            }
            else{
                var content = '<p id="warning-message" class="text-center lead">The team dont have projects. Please add one to start</p>'
                $( "#projects" ).append(content);
            }
        },
        error : function(data) {
            console.log('ERROR:',data)
        }
    });   
})