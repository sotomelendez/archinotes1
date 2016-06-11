$(document).ready(function() {
    $('#simple-menu').sidr();
    $('#top_menu a').each(function() {
        $(this).removeClass('active');
    });
    $('#operations').addClass('active');
    $('#id_operational_scenarios option:first').attr('selected','selected');
    $('#id_operational_scenarios').trigger('change');
    $('.delete_operational_scenario_cancel').click(function() {
        $('#modal_delete_operational_scenario #text_to_replace').text('Are you sure you want to delete name_to_replace ?');
    });
});
$('#id_operations_form').validate({
    rules:{
        stakeholder_description:{
            required:true,
        },
        context:{
            required:true,
        },
        context_description:{
            required:true,
        },
        functionality:{
            required:true,
        },
        functionality_description:{
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
$('#id_operations_form').submit(function(event) { 
    $('#id_inputs option').prop('selected', true);
    $('#id_outputs option').prop('selected', true);
});
function addInput(){
    var input_name = $('#id_input_name').val();
    var inputs = $('#id_inputs').find('option').map(function() {return this.value;});
    var temp = true;
    if(input_name!=null&&input_name.length>0){
        for(i=0;i<inputs.length;i++){
            if(input_name==inputs[i]){
                temp = false;
            }
        }
    }
    if(temp){
        var value = input_name.replace(/ /g,"_")
        var content = $("<option value="+value+">"+input_name+"</option>");                   
        $('#id_inputs').append($(content));
        $('#id_input_name').val('');
    }
};
function addOutput(){
    var input_name = $('#id_output_name').val();
    var inputs = $('#id_outputs').find('option').map(function() {return this.value;});
    var temp = true;
    if(input_name!=null&&input_name.length>0){
        for(i=0;i<inputs.length;i++){
            if(input_name==inputs[i]){
                temp = false;
            }
        }
    }
    if(temp){
        var value = input_name.replace(/ /g,"_")
        var content = $("<option value="+value+">"+input_name+"</option>");                   
        $('#id_outputs').append($(content));
        $('#id_output_name').val('');
    }
};
$('#id_operational_scenarios').change(function () {
    var name = $('#id_operational_scenarios').val();
    var url_value = $('#id_url_get_value').val();
    if(name!=null&&name.length>0){
        $.ajax({
            dataType : 'json',
            url : url_value,
            type : 'GET',
            data : {'name':name},
            success : function(data) {
                var response = data['success']
                if(response!=null){
                    $("#id_stakeholders option").filter(function() {
                        return $(this).text() == response['stakeholder']; 
                    }).prop('selected', true);
                    $('#id_stakeholder_description').val(response['stakeholder_description']);
                    $('#id_context').val(response['context']);
                    $('#id_context_description').val(response['context_description']);
                    $('#id_inputs').empty();
                    $('#id_outputs').empty();
                    for(i=0;i<response['inputs'].length;i++){
                        var value = response['inputs'][i].replace(/ /g,"_")
                        var content = $("<option value="+value+">"+response['inputs'][i]+"</option>");                   
                        $('#id_inputs').append($(content));
                    }
                    $('#id_functionality').val(response['functionality']);
                    $('#id_functionality_description').val(response['functionality_description']);
                    for(i=0;i<response['outputs'].length;i++){
                        var value = response['outputs'][i].replace(/ /g,"_")
                        var content = $("<option value="+value+">"+response['outputs'][i]+"</option>");                   
                        $('#id_outputs').append($(content));
                    }
                }
            },
            error: function (data) {
            }
        });
    }
});
function deleteOperationalScenario(){
    var operational_scenario_name = $('#id_operational_scenarios').val();
    if(operational_scenario_name == undefined)
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
    else if(operational_scenario_name.length>0){
        var text = $('#modal_delete_operational_scenario #text_to_replace').text();
        text = text.replace('name_to_replace', operational_scenario_name);
        $('#modal_delete_operational_scenario #text_to_replace').text(text);
        $('#modal_delete_operational_scenario #name').val(operational_scenario_name);
        $('#modal_delete_operational_scenario').modal('show');
    }
}