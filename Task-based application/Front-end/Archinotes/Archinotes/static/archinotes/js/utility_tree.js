$(document).ready(function() {
    $('#simple-menu').sidr();
    $('#top_menu a').each(function() {
        $(this).removeClass('active');
    });
    $('#utility_tree').addClass('active');
    $('#tree').orgChart({container: $('#chart-container'),nodeClicked: onChartNodeClicked,});
    $('.delete_node_utility_tree').click(function() {
        var url_value = $('#id_delete_url').val();
        $('#form_update_node_utility_tree').attr('action',url_value);
    });
    $('.delete_utility_tree').click(function() {
        var url_value = $('#id_d_url').val();
        $('#form_update_utility_tree').attr('action',url_value);
    });
    $('.add_utility_tree').click(function() {
        var url_value = $('#id_a_url').val();
        $('#form_update_utility_tree').attr('action',url_value);
    });
});
function onChartNodeClicked(node) {
    var node_clicked = node.attr('id').split('::');
    if(node_clicked.length==1 && node_clicked[0]!='tree_head'){
        var qa_name = node_clicked[0];
        $('#id_old_qa_name').val(qa_name);
        $('#id_name_qa').val(qa_name);
        var url_value = $('#id_u_url').val();
        $('#form_update_utility_tree').attr('action',url_value);
        $('#modal_update_utility_tree').modal('show');
    }
    else if(node_clicked.length==1 && node_clicked[0]=='tree_head'){
        $('#modal_add_utility_tree_node').modal('show');
    }
    else if(node_clicked.length==3){
        var qa_name = node_clicked[0];
        var qa_node_name = node_clicked[1];
        var qa_node_score = node_clicked[2];
        $('#id_qa_name').val(qa_name);
        $('#id_qa_node_name').val(qa_node_name);
        $('#id_qa_node_score').val(qa_node_score);
        var score = node_clicked[2].split(' ');
        $("#id_stakeholder_priority option").filter(function() {
            return $(this).text() == score[0]; 
        }).prop('selected', true);
        $("#id_implementation_difficulty option").filter(function() {
            return $(this).text() == score[1]; 
        }).prop('selected', true);
        $('#modal_update_node_score_utility_tree').modal('show');
    }
    else if(node_clicked.length==2){
        var qa_name = node_clicked[0];
        var qa_node_name = node_clicked[1];
        $('#id_qa_u_name').val(qa_name);
        $('#id_qa_u_node_name').val(qa_node_name);
        $('#id_name').val(qa_node_name);
        var url_value = $('#id_update_url').val();
        $('#form_update_node_utility_tree').attr('action',url_value);
        $('#modal_update_node_utility_tree').modal('show');
    }
}