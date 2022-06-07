$(document).ready(function () {
  console.log('Loading')
  $('#feedbackbtnsm').click(function () {
    $(this).
  })

function postFeedback(feedback)
  data = {'feedback': feedback}
  ajax({
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
