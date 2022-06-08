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


  })

  // Register

  $('#registerbtn').click(function (e) {
    e.preventDefault();

    if($('#regpassword').val().length > 6){
      if($('#regpassword').val() === $('#checkpassword').val()) {
        console.log('Password Checked');



      }else{
        console.log($('#regpassword').val() + "  uhigugyyu" + $('#checkpassword').val())
        alert('Password does not match')
      }

    }else{
      $('#regpassword').addClass('is-invalid')
      
    }




    let data = $('#regform').serialize();
    console.log(data);
  })

})
