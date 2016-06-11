$(document).ready(function(){
    var login_form = $('#id_sign_in_form');
    if(login_form != undefined) {
        $(login_form).validate({
            rules:{
                email:{
                    required:true,
                },
                password:{
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
                        placement: 'bottom',
                        content: value.message,
                        template: '<div class="popover error"><div class="arrow error"></div><div class="popover-inner"><div class="popover-content error"><p></p></div></div></div>'
                    });
                    _popover.data('bs.popover').options.content = value.message;
                    $(value.element).popover('show');
                    $(value.element).closest('.control-group').removeClass('success').addClass('error');
                });
            }
        });
    }
});