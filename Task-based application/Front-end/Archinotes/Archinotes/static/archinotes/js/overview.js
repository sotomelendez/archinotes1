$(document).ready(function() {
    $('#simple-menu').sidr();
    $('#top_menu a').each(function() {
        $(this).removeClass('active');
    });
    $('#overview').addClass('active');
});
$('#id_overview_form').validate({
    rules:{
        background:{
            required:true,
        },
        purpose_scope:{
            required:true,
        },
        overview:{
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