$(document).ready(function () {

  let token = localStorage.getItem('glideceylontoken')
  let csrf_token = $("[name=csrfmiddlewaretoken]").val()
  console.log(csrf_token)
  console.log(token)
  $.post({
    url:'/auth/user/verify/token',
    data: {csrfmiddlewaretoken: csrf_token, token: token},
    success: function (data, status) {
      if(data.status === 404){
        console.log('flkeqhiugjhdbeKFAEGVYUG')
        $('#signinpathbtn').removeClass('d-none')
        $('#signinpathbtn2').removeClass('d-none')
      }else if(data.status === 200){
        let userid = data.userid
        let name = data.name
        let email = data.email
        let fstletter = name.charAt(0).toUpperCase()

        $('#navbarScrollingDropdown').html(fstletter)
        $('#navlogedname').html(name)
        $('#navlogedemail').html(email)
        $('#navlogout').html("<a class='dropdown-item text-danger' href='/auth/user/logout?token="+token+"' >Log Out</a>")
        $('#navmyacc').removeClass('d-none')
        $('#navmyacchref').attr('href', '/account/' + userid)
        $('#logedintab').removeClass('d-none')
      }
    }
  })


  $('#feedbackbtnsm').click(function () {
    let feedback = $('#feedbacktxtsm').val()
    if(feedback != '') {
      postFeedback(feedback)
    }

  });


  $('#feedbackbtnlg').click(function () {
    let feedback = $('#feedbacktxtlg').val()
    if(feedback != '') {
      postFeedback(feedback)
    }
  });



function postFeedback(feedback){
  let data = {feedback: feedback}
  $.ajax({
          type: "GET",
          url: "/post/user/feedback",
          data: data,
          success: function(data, status){
            if (status == 400){
            }else{
              alert(data.success + ' Thanks! for your kindness')
              $('#feedbacktxtsm').val('')
              $('#feedbacktxtlg').val('')
            }
          }
        });
}
});
