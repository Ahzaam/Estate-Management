
$(document).ready(function () {
  $('#confirm').click(function (e) {
    e.preventDefault();
    data = $('#idconfirm').serialize();

    $.post({
      url: '/account/id/confirm/password',
      data: data,
      success: function (data, status) {
        if(data.status == 200){
          window.location.reload();
        }else{
          $('#inputPassword2').addClass('is-invalid');
        }
      }
    })
  })
})
