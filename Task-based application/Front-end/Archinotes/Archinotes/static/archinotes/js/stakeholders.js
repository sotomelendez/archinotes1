$(document).ready(function() {
    $('#simple-menu').sidr();
    $('#top_menu a').each(function() {
        $(this).removeClass('active');
    });
    $('#stakeholders').addClass('active');
    $( '.drag' ).draggable({containment:'#panel'});
    $('.add_stakeholder_cancel').click(function() {
        var url_value = $('#id_url_new_value').val();
        $('#add_stakeholder_form').attr('action',url_value);
        $('#add_stakeholder_add').text('Add');
        $('#id_name').val('');
        $("#id_stakeholders_types").val($("#id_stakeholders_types option:first").val());
        $('#id_concerns').empty();
        $('#modal_add_stakeholder_label').text('New stakeholder')
    });
    $('.delete_stakeholder_cancel').click(function() {
        $('#modal_delete_stakeholder #text_to_replace').text('Are you sure you want to delete name_to_replace ?');
    });
});
function toggleBtn(btn_id){
    if($('#'+btn_id).hasClass('active')){
        $('#'+btn_id).removeClass('active');
    } 
    else{
        $('#stakeholders_panel a').each(function() {
            $(this).removeClass('active');
        });
        $('#'+btn_id).addClass('active');
    }
}
function updateStakeholder(){
    var name = $('a.btn.btn-default.circle.drag.active').attr('id');
    if(name == undefined)
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
        modal += '<p>Please select a stakeholder!</p>';
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
    else if(name.length>0){
        var project_name = $('#id_project_name').val();
        var url_value = $('#id_url_get_value').val();
        $.ajax({
            dataType : 'json',
            url : url_value,
            type : 'GET',
            data : {'name':name,'project_name':project_name},
            success : function(data) {                   
                name = data['success']['name']
                type = data['success']['type']
                concerns = data['success']['concerns']
                $('#id_name').val(name);
                $('#id_old_name').val(name);
                $('#modal_add_stakeholder_label').text('Update stakeholder')
                $('#add_stakeholder_add').text('Update');
                $('#id_concerns').empty();
                for(i=0;i<concerns.length;i++){
                    var value = concerns[i].replace(/_/g," ")
                    var content = $("<option value="+concerns[i]+">"+value+"</option>");                   
                    $('#id_concerns').append($(content));
                }
                $("#id_stakeholders_types option").filter(function() {
                    return $(this).text() == type; 
                }).prop('selected', true);
                var url_value = $('#id_url_update_value').val();
                $('#add_stakeholder_form').attr('action',url_value);
                $('#modal_add_stakeholder').modal('show');
            },
            error: function (data) {
                console.log('error',data)
            }
        });
    }
}
function deleteStakeholder(){
    var stakeholder_id = $('a.btn.btn-default.circle.drag.active').attr('id');
    if(stakeholder_id == undefined)
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
        modal += '<p>Please select a stakeholder!</p>';
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
    else if(stakeholder_id.length>0){
        var stakeholder_name = $('a.btn.btn-default.circle.drag.active').attr('id')
        var text = $('#modal_delete_stakeholder #text_to_replace').text();
        text = text.replace('name_to_replace', stakeholder_name);
        $('#modal_delete_stakeholder #text_to_replace').text(text);
        $('#modal_delete_stakeholder #name').val(stakeholder_name);
        $('#modal_delete_stakeholder').modal('show');
    }
}
function addConcern(){
    var name = $('#id_concern_description').val();
    if(name==null||name.length==0){
        $('#id_concern_description').attr('placeholder', 'Name can´t be blank');
    }
    else if(name!=null&&name.length>0){
        var value = name.replace(/ /g,'_')
        var content = $("<option value="+value+">"+name+"</option>");                   
        $('#id_concerns').append($(content));
        $('#id_concern_description').attr('placeholder', '');
        $('#id_concern_description').val('');
    }
};
function deleteConcern(){
    $('#id_concerns option:selected').remove()
};
$('#add_stakeholder_form').submit(function( event ) {
    $("#id_concerns option").attr("selected", "selected");
});