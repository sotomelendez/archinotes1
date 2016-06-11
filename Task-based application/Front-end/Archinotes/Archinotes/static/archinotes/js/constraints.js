$(document).ready(function() {
    $('#simple-menu').sidr();
    $('#top_menu a').each(function() {
        $(this).removeClass('active');
    });
    $('#constraints').addClass('active');
    $('.add_constraint_cancel').click(function() {
        var url_value = $('#id_url_new_value').val()
        $('#add_constraint_form').attr('action',url_value);
        $('#add_constraint_add').text('Add');
        $('#id_name').val('');
        $("#id_stakeholders").val($("#id_stakeholders option:first").val());
        $("#id_types").val($("#id_types option:first").val()); 
        $('#id_description').val('');
        $('#id_alternatives').val('');
        $('#modal_add_constraint_label').text('New constraint')
    });
});
$('#tbody_kits tr').click(function () {
    if($(this).hasClass('active')){
        $(this).removeClass('active');
    }
    else{
        $('#tbody_kits tr').removeClass('active');
        $(this).addClass('active');  
    }
});
function updateConstraint(){
    var constraint_name = $('#tbody_kits tr.active').attr('id');
    if(constraint_name == undefined)
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
        modal += '<p>Please select a constraint!</p>';
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
    else if(constraint_name.length>0){
        var row = $('#tbody_kits tr.active td');
        var type = row[0].id;
        var name = row[1].id;
        var stakeholder = row[2].id;
        var description = row[3].id;
        var alternatives = row[4].id;
        $('#id_name').val(name);
        $('#id_old_name').val(name);
        $('#modal_add_constraint_label').text('Update constraint')
        $('#add_constraint_add').text('Update');
        $("#id_types option").filter(function() {
            return $(this).text() == type; 
        }).prop('selected', true);
        $("#id_stakeholders option").filter(function() {
            return $(this).text() == stakeholder; 
        }).prop('selected', true);
        $('#id_description').val(description);
        $('#id_alternatives').val(alternatives);
        var url_value = $('#id_url_update_value').val()
        $('#add_constraint_form').attr('action',url_value);
        $('#modal_add_constraint').modal('show');
    }
}
function deleteConstraint(){
    var constraint_name = $('#tbody_kits tr.active').attr('id');
    if(constraint_name == undefined)
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
        modal += '<p>Please select a constraint!</p>';
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
    else if(constraint_name.length>0){
        var text = $('#modal_delete_constraint #text_to_replace').text();
        text = text.replace('name_to_replace', constraint_name);
        $('#modal_delete_constraint #text_to_replace').text(text);
        $('#modal_delete_constraint #name').val(constraint_name);
        $('#modal_delete_constraint').modal('show');
    }
}