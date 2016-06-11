$(document).ready(function() {
    $('#simple-menu').sidr();
    $('#top_menu a').each(function() {
        $(this).removeClass('active');
    });
    $('#quality_requirements').addClass('active');
    var element = $('#quality_atributes a:first')
    element.addClass('active');
    onChangeList(element.attr('id'))
    
    $('.new_quality_requirement').click(function() {
        var ans = $( "a.list-group-item.active" ).attr('id').split('-')
        $('#id_quality_atribute').val(ans[0]);
        $('#id_quality_atribute_node').val(ans[1]);
    });
    $('.update_quality_scenarios').click(function() {
        var url_value = $('#id_url_update_value').val();
        $('#form_update_quality_scenarios').attr('action',url_value);
        var ans = $( "a.list-group-item.active" ).attr('id').split('-')
        $('#id_quality_atribute').val(ans[0]);
        $('#id_quality_atribute_node').val(ans[1]);
    });
});
function onChangeList(item){
    $('#quality_atributes a').each(function() {
        $(this).removeClass('active');
    });
    $('#'+item).addClass('active');
    var url_value = $('#id_url_get_value').val();
    var ans = $( "a.list-group-item.active" ).attr('id').split('-')
    $('#quality_scenarios').empty();
    $.ajax({
        dataType : 'json',
        url : url_value,
        type : 'GET',
        data : {'quality_atribute':ans[0],'quality_atribute_node':ans[1]},
        success : function(data) {  
            var response = data['success'];
            if(response!=null){
                quality_scenarios = response[0]['quality_scenarios'];
                if(quality_scenarios.length>0){
                    var quality_atribute = response[0]['quality_atribute'];
                    var quality_atribute_node = response[0]['quality_atribute_node'];
                    for(i=0;i<quality_scenarios.length;i++){
                        var name = quality_scenarios[i]['name'];
                        var source = quality_scenarios[i]['source'];
                        var stimulus = quality_scenarios[i]['stimulus'];
                        var artifact = quality_scenarios[i]['artifact'];
                        var enviroment = quality_scenarios[i]['enviroment'];
                        var response = quality_scenarios[i]['response'];
                        var response_measure = quality_scenarios[i]['response_measure'];
                        var url_delete_value = $('#id_url_delete_value').val();
                        var url_update_value = $('#id_url_update_value').val();
                        var content = '<form id="form_update_quality_scenarios" action="'+url_update_value+'" method="post" class="form-horizontal">';
                        content += '<input id="id_qa_name" type="hidden" name="qa_name" value="'+quality_atribute+'">';
                        content += '<input id="id_qa_node_name" type="hidden" name="qa_node_name" value='+quality_atribute_node+'>';
                        content += '<input id="id_qs_name" type="hidden" name="qs_name" value='+name+'>';
                        content += '<div class="panel panel-default">';
                        content += '<div class="panel-heading">';
                        content += '<h4 class="panel-title"><a id="id_qs_title" data-toggle="collapse" data-parent="#accordion" href="#'+name+'">'+name+'</a></h4>';
                        content += '</div>';
                        content += '<div id="'+name+'" class="panel-collapse collapse">';
                        content += '<div class="panel-body">';
                        content += '<div class="col-md-12">';
                        content += '<div class="col-md-5">';
                        content += '<div class="col-md-6">';
                        content += '<div class="panel panel-default quality">';
                        content += '<div class="panel-body source text-center">';
                        content += '<h4 class="no-margin harabara">Source</h4><i class="fa fa-users fa-5x bottom-top-padding"></i>';
                        content += '<textarea id="id_source" name="source" class="circle form-control">'+source+'</textarea>';
                        content += '</div>';
                        content += '</div>';
                        content += '</div>';
                        content += '<div class="col-md-6">';
                        content += '<div class="panel panel-default quality">';
                        content += '<div class="panel-body stimulus text-center">';
                        content += '<h4 class="no-margin harabara">Stimulus</h4><i class="fa fa-bolt fa-5x bottom-top-padding"></i>';
                        content += '<textarea id="id_stimulus" name="stimulus" class="circle form-control">'+stimulus+'</textarea>';
                        content += '</div>';
                        content += '</div>';
                        content += '</div>';
                        content += '</div>';
                        content += '<div class="col-md-2">';
                        content += '<div class="panel panel-default middle">';
                        content += '<div class="panel-body artifact text-center">';
                        content += '<h4 class="no-margin harabara">Artifact</h4>';
                        content += '<textarea id="id_artifact" name="artifact" class="circle form-control">'+artifact+'</textarea>';
                        content += '</div>';
                        content += '</div>';
                        content += '<div class="panel panel-default middle">';
                        content += '<div class="panel-body enviroment text-center">';
                        content += '<h4 class="no-margin harabara">Enviroment</h4>';
                        content += '<textarea id="id_enviroment" name="enviroment" class="circle form-control">'+enviroment+'</textarea>';
                        content += '</div>';
                        content += '</div>';
                        content += '</div>';
                        content += '<div class="col-md-5">';
                        content += '<div class="col-md-6">';
                        content += '<div class="panel panel-default quality">';
                        content += '<div class="panel-body response text-center">';
                        content += '<h4 class="no-margin harabara">Response</h4><i class="fa fa-envelope fa-5x bottom-top-padding"></i>';
                        content += '<textarea id="id_response" name="response" class="circle form-control">'+response+'</textarea>';
                        content += '</div>';
                        content += '</div>';
                        content += '</div>';
                        content += '<div class="col-md-6">';
                        content += '<div class="panel panel-default quality">';
                        content += '<div class="panel-body response-measure text-center">';
                        content += '<h4 class="no-margin harabara">Response Measure</h4><i class="fa fa-tachometer fa-5x bottom-padding"></i>';
                        content += '<textarea id="id_response_measure" name="response_measure" class="circle form-control">'+response_measure+'</textarea>';
                        content += '</div>';
                        content += '</div>';
                        content += '</div>';
                        content += '</div>';
                        content += '</div>';
                        content += '<div class="col-md-12 bottom-margin">';
                        content += '<div class="col-md-6 text-right harabara">';
                        content += '<button type="submit" class="btn btn-success update_quality_scenarios">Save</button>';
                        content += '</div>';
                        content += '</div>';
                        content += '</div>';
                        content += '</div>';
                        content += '</div>';
                        content += '</form>';
                        $('#quality_scenarios').append(content);
                    }
                }
                else{
                    var content = '<p id="warning-message" class="text-center lead">The quality atribute dont have quality scenarios. Please add one to start</p>'
                    $('#quality_scenarios').append(content);
                }
            }                 
        },
        error: function (data) {
            console.log('error',data)
        }
    });
}