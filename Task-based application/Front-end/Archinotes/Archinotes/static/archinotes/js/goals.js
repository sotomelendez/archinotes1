$("#id_goals_form").validate({
    rules:{
        goal:{
            required:true,
        },
        objective:{
            required:true,
        },
        driver:{
            required:true,
        }
    },
    showErrors: function (errorMap, errorList) {
        $.each(this.successList, function (index, value) {
            $(value).popover('hide');
            $(value).closest('.control-group').removeClass('error').addClass('success');
        });
        return $.each(errorList, function (index, value) {
            var _popover = $(value.element).popover({
                trigger: 'manual',
                placement: 'top',
                content: value.message,
                template: '<div class="popover error"><div class="arrow error"></div><div class="popover-inner"><div class="popover-content error"><p></p></div></div></div>'
            });
            _popover.data('bs.popover').options.content = value.message;
            $(value.element).popover('show');
            $(value.element).closest('.control-group').removeClass('success').addClass('error');
        });
    }
});
var min_range = $('#id_minimum').val();
var max_range = $('#id_maximum').val();
$(document).ready(function() {
    $('#simple-menu').sidr();
    $('#top_menu a').each(function() {
        $(this).removeClass('active');
    });
    $('#goals').addClass('active');
    drawSlider(33, 66, min_range, max_range);
    $("#id_business_goals option:first").attr('selected','selected');
    $('#id_business_goals').trigger('change');
    $('.delete_business_goal_cancel').click(function() {
        $('#modal_delete_business_goal #text_to_replace').text('Are you sure you want to delete name_to_replace ?');
    });
});
google.load('visualization', '1.0', {'packages':['corechart']});
google.setOnLoadCallback(drawChart);
function drawChart(min, med, max) {
    if(min>0&&med>0&&max>0){
        $('#id_chart_min').val(min);
        $('#id_chart_med').val(med);
        $('#id_chart_max').val(max);
        var data = google.visualization.arrayToDataTable([
            ['Measure', 'Measure Ranges'],
            ['LOW',  min],
            ['MEDIUM',  med],
            ['HIGH', max],
        ]); 
    }
    else{
        var data = google.visualization.arrayToDataTable([
            ['Measure', 'Measure Ranges'],
            ['FAIL',  33],
            ['ALMOST',  33],
            ['SUCCESS', 33],
        ]);        
    }
    var options = {
        'legend': 'none',
        'pieSliceText': 'label',
        'width':150,
        'height':170,
        'pieStartAngle':180,
        'chartArea': {'width': '90%', 'height': '90%'},
        'colors': ['#BE0000', '#FD8A0B', '#7AB73E']
    };
    var chart = new google.visualization.PieChart($('#chart_div')[0]);
    chart.draw(data, options);
}
function drawSlider(fromx, tox, min, max) {
    $("#id_slider").ionRangeSlider({
        min: min,
        max: max,
        from: fromx,
        to: tox,
        type: 'double',
        step: 1,
        prettify: true,
        hasGrid: true,
        onChange: function (obj) {
            min=obj['fromNumber'];
            max=100-obj['toNumber'];
            med=100-max-min;
            drawChart(min,med,max);
        },
    });
}
$('#id_goals_form').submit(function(event) { 
    $("#id_quality_atributes option").attr("selected", "selected");
    $("#id_stakeholders option").attr("selected", "selected");
});
$( "#id_minimum" ).change(function () {
    min_range = $('#id_minimum').val();
    $('#range_slider').empty();
    var content = '<input id="id_slider" name="slider" type="text"></input>';
    $('#range_slider').append(content);
    drawSlider(33, 66, min_range, max_range);
});
$( "#id_maximum" ).change(function () {
    max_range = $('#id_maximum').val();
    $('#range_slider').empty();
    var content = '<input id="id_slider" name="slider" type="text"></input>';
    $('#range_slider').append(content);
    drawSlider(33, 66, min_range, max_range);
});
$( "#id_business_goals" ).change(function () {
    var name = $('#id_business_goals').val();
    var project_name = $('#id_business_goals').val();
    var url_value = $('#id_url_get_value').val();
    if(name!=null&&name.length>0){
        $.ajax({
            dataType : 'json',
            url : url_value,
            type : 'GET',
            data : {'name':name,'project_name':project_name},
            success : function(data) {
                var response = data['success'];
                if(response!=null){
                    $('#id_goal').val(response['goal_description']);
                    $('#id_objective').val(response['objective']);
                    $('#id_driver').val(response['driver']);
                    $('#id_stakeholders').empty();
                    $('#id_quality_atributes').empty();
                    for(i=0;i<response['stakeholders'].length;i++){
                        var value = response['stakeholders'][i].replace(/ /g,"_")
                        var content = $("<option value="+value+">"+response['stakeholders'][i]+"</option>");                   
                        $('#id_stakeholders').append($(content));
                    }
                    for(i=0;i<response['quality_atributes'].length;i++){
                        var value = response['quality_atributes'][i].replace(/ /g,"_")
                        var content = $("<option value="+value+">"+response['quality_atributes'][i]+"</option>");                   
                        $('#id_quality_atributes').append($(content));
                    }
                    $("#id_measures option").filter(function() {
                        return $(this).text() == response['measure']; 
                    }).prop('selected', true);
                    drawChart(response['chart_min'],response['chart_med'],response['chart_max']);
                    min_range = response['range_min'];
                    max_range = response['range_max'];
                    $('#id_minimum').val(response['range_min']);
                    $('#id_maximum').val(response['range_max']);
                    $('#range_slider').empty();
                    var content = '<input id="id_slider" name="slider" type="text"></input>';
                    $('#range_slider').append(content);
                    drawSlider(33, 66, min_range, max_range);
                }
            },
            error: function (data) {
            }
        });
    }
});
function addStakeholder(){
    var stakeholders_types = $('#id_stakeholders_types').val();
    var stakeholders = $('#id_stakeholders').find('option').map(function() {return this.value;});
    var temp = true;
    if(stakeholders_types!=null&&stakeholders_types.length>0){
        for(i=0;i<stakeholders.length;i++){
            if(stakeholders_types==stakeholders[i]){
                temp = false;
            }
        }
    }
    if(temp){
        var value = stakeholders_types.replace(/ /g,"_")
        var content = $("<option value="+value+">"+stakeholders_types+"</option>");                   
        $('#id_stakeholders').append($(content));
    }
};
function deleteStakeholder(){
    $('#id_stakeholders option:selected').remove()
};
function addQualityAttribute(){
    var quality_atributes_types = $('#id_quality_atributes_types').val();
    var quality_atributes = $('#id_quality_atributes').find('option').map(function() {return this.value;});
    var temp = true;
    if(quality_atributes_types!=null&&quality_atributes_types.length>0){
        for(i=0;i<quality_atributes.length;i++){
            if(quality_atributes_types==quality_atributes[i]){
                temp = false;
            }
        }
    }
    if(temp){
        var value = quality_atributes_types.replace(/ /g,"_")
        var content = $("<option value="+value+">"+quality_atributes_types+"</option>");                   
        $('#id_quality_atributes').append($(content));
    }
};
function deleteQualityAttribute(){
    $('#id_quality_atributes option:selected').remove()
};
function deleteBusinessGoal(){
    var business_goal_name = $('#id_business_goals').val();
    if(business_goal_name == undefined)
    {
        var modal = '<div class="modal fade" id="modify_utility_tree_modal" tabindex="-1" role="dialog" aria-labelledby="modify_utility_tree_modal_Label" aria-hidden="true">';
        modal += '<div class="modal-dialog modal-sm">';
        modal += '<div class="modal-content">';
        modal += '<div class="modal-header">';
        modal += '<button type="button" class="close" data-dismiss="modal" aria-hidden="true"><i class="fa fa-times"></i></button>';
        modal += '<h4 class="modal-title">Warning!</h4>';
        modal += '</div>';
        modal += '<div class="modal-body">';
        modal += '<div class="form-horizontal">';
        modal += '<div class="form-group">';
        modal += '<div class="col-md-12">';
        modal += '<p>Please select a business goal!</p>';
        modal += '</div>';
        modal += '</div>';
        modal += '<div class="form-group">';
        modal += '<div class="col-md-12 text-center harabara">';
        modal += '<input type="reset" class="btn btn-primary" data-dismiss="modal" value="Accept"></input>';
        modal += '</div>';
        modal += '</div>';
        modal += '</div>';
        modal += '</div>';
        modal += '</div>';
        modal += '</div>';
        modal += '</div>';
        $('#modals').empty();
        $('#modals').append(modal);
        $('#modify_utility_tree_modal').modal('show');
    }
    else if(business_goal_name.length>0){
        var text = $('#modal_delete_business_goal #text_to_replace').text();
        text = text.replace('name_to_replace', business_goal_name);
        $('#modal_delete_business_goal #text_to_replace').text(text);
        $('#modal_delete_business_goal #name').val(business_goal_name);
        $('#modal_delete_business_goal').modal('show');
    }
}