$(document).ready(function() {

  $('#change1').click(function() {
    $('#formContentregister').show()
    $('#formContentsignin').hide()
  });

  $('#change2').click(function(){
    $('#formContentregister').hide()
    $('#formContentsignin').show()
  })

  // Login


  $('#loginbtn').click(function (e) {
    e.preventDefault();

    let data = $('#logform').serialize();
    console.log(data);
    $.post({
      url:'/auth/user/login',
      data: data,
      success: function (data, status) {
        if(data.status === 204) {
          $('#logemailerror').html('Account Doesnt Exist')
          $('#logemail').addClass('is-invalid')
        }else if(data.status === 401){
          $('#logemailerror').html('Email or Password Incorrect')
          $('#logemail').addClass('is-invalid')
          $('#logpassword').addClass('is-invalid')
        }else if(data.status === 200){
          localStorage.removeItem('glideceylontoken')
          localStorage.setItem('glideceylontoken', data.token)
          window.location.href = '/'
        }
      }
    })

  })

  // Register

  $('#registerbtn').click(function (e) {
    e.preventDefault();

    if($('#nameper').val() != ''){
      if($('#regpassword').val().length > 6){

        if($('#regpassword').val() === $('#checkpassword').val()) {
          let data = $('#regform').serialize()
          if($('#inputcity').val() === '' ||  $('#inputstate').val() === 'Choose...'){
            if($('#inputcity').val() === ''){
              $('#inputcity').addClass('is-invalid')
            }else{
              $('#inputstate').addClass('is-invalid')
            }
          }else{
            $('#registerbtn').addClass('disabled')
            $.post({
              url: '/auth/user/register',
              data: data,
              success: function (data, status){
                console.log(data.status)
                console.log(status)
                if(data.status === 202){
                  $('#otpsec').removeClass('d-none')
                }
                if(data.status === 226){
                  $('#email').addClass('is-invalid')
                  $('#emailerror').html('Email Already Exist')
                  $('#registerbtn').removeClass('disabled')
                }
              }
            })
          }



        }else{
          console.log($('#regpassword').val() + "  uhigugyyu" + $('#checkpassword').val())
          $('#passworderror').html('Password Doesnt Match');
          $('#regpassword').addClass('is-invalid')
          $('#checkpassword').addClass('is-invalid')
        }


      }else{
        $('#passworderror').html('Password is too short')
        $('#regpassword').addClass('is-invalid')

      }
    }else{
      $('#nameper').addClass('is-invalid')
    }

    $('#confotpbtn').click(function (e) {
      e.preventDefault()
      $('#confotpbtn').addClass('disabled')
      let otpveri = $('#otpform').serialize()
      console.log($('#otpform').serialize())
      $.post({
        url: '/auth/user/verify/otp',
        data: otpveri,
        success: function (data, status){
          console.log(data.status + ' ' + status)
          if(data.status === 200 ){
            name = $('#nameper').val()
            email = $('#email').val()
            $('#sucname').html(name)
            $('#sucemail').html(email)
            $('#form-container').hide()
            $('#regredirect').removeClass('d-none')
          }else{
            $('#confotp').addClass('is-invalid')
            $('#confotpbtn').removeClass('disabled')
          }

        }
      })
    })


  })

})
