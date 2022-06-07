$(document).ready(function () {


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
            if (status == 200){
              $(this).html('&nbsp Submit &nbsp')
              console.log('Successfully posted')
            }
            else{

              alert(data.success)
            }
          }
        });
}
});
