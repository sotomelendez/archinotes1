$(document).ready(function(){
    var id_sign_up_form = $('#id_sign_up_form');
    if(id_sign_up_form != undefined) {
        $(id_sign_up_form).validate({
            rules:{
                email:{
                    required:true,
                },
                email_confirm:{
                    required:true,
                },
                password:{
                    required:true,
                },
                password_confirm:{
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
                        placement: 'right',
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
    $("#id_email_confirm").keyup(checkEmailMatch);
    $("#id_password_confirm").keyup(checkPasswordMatch);
});
function checkEmailMatch() {
    var email = $("#id_email_sign_up").val();
    var confirmEmail = $("#id_email_confirm").val();
    console.log('email',email,'confirmEmail',confirmEmail)
    if(email == confirmEmail && email.length > 0 && confirmEmail.length > 0){
        var _popover = $('#id_email_confirm').popover({
            trigger: 'manual',
            placement: 'right',
            content: 'Emails match!',
            template: '<div class="popover error"><div class="arrow error"></div><div class="popover-inner"><div class="popover-content error"><p></p></div></div></div>'
        });
        _popover.data('bs.popover').options.content = 'Emails match!';
        $('#id_email_confirm').popover('show');
        $('#id_email_confirm').closest('.control-group').removeClass('success').addClass('error');
    }
    else{
        var _popover = $('#id_email_confirm').popover({
            trigger: 'manual',
            placement: 'right',
            content: 'Emails do not match!',
            template: '<div class="popover error"><div class="arrow error"></div><div class="popover-inner"><div class="popover-content error"><p></p></div></div></div>'
        });
        _popover.data('bs.popover').options.content = 'Emails do not match!';
        $('#id_email_confirm').popover('show');
        $('#id_email_confirm').closest('.control-group').removeClass('success').addClass('error');
    }
}
function checkPasswordMatch() {
    var password = $("#id_password_sign_up").val();
    var confirmPassword = $("#id_password_confirm").val();
    if(password == confirmPassword && password.length > 0 && confirmPassword.length > 0){
        var _popover = $('#id_password_confirm').popover({
            trigger: 'manual',
            placement: 'right',
            content: 'Passwords match!',
            template: '<div class="popover error"><div class="arrow error"></div><div class="popover-inner"><div class="popover-content error"><p></p></div></div></div>'
        });
        _popover.data('bs.popover').options.content = 'Passwords match!';
        $('#id_password_confirm').popover('show');
        $('#id_password_confirm').closest('.control-group').removeClass('success').addClass('error');
    }
    else{
        var _popover = $('#id_password_confirm').popover({
            trigger: 'manual',
            placement: 'right',
            content: 'Passwords do not match!',
            template: '<div class="popover error"><div class="arrow error"></div><div class="popover-inner"><div class="popover-content error"><p></p></div></div></div>'
        });
        _popover.data('bs.popover').options.content = 'Passwords do not match!';
        $('#id_password_confirm').popover('show');
        $('#id_password_confirm').closest('.control-group').removeClass('success').addClass('error');
    }
}