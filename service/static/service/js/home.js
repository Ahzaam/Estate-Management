$(document).ready(function() {

  var inView = false;

  function isScrolledIntoView(elem)
  {
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();

    var elemTop = $(elem).offset().top;
  var elemBottom = elemTop + $(elem).height();

  return ((elemTop <= docViewBottom) && (elemBottom >= docViewTop));
}

$(window).scroll(function() {
    if (isScrolledIntoView('#fec')) {
      if (inView) { return; }
      inView = true;
      console.log('')
      myLoop();
    } else {

      inView = false;
    }
  });


  // console.log('  #ac' + i)
  var i = 1;                  //  set your counter to 1

  function myLoop() {         //  create a loop function
    setTimeout(function() {   //  call a 3s setTimeout when the loop is called
      $('#ac'+i).css('opacity', 1)   //  your code here
      $('#ac'+i).css('transform', 'translateX(0)')
      i++;                    //  increment the counter
      if (i < 5) {           //  if the counter < 10, call the loop function
        myLoop();             //  ..  again which will trigger another
      }                       //  ..  setTimeout()
    }, 200)
  }

  j = 1;
  function myLoopFeature() {         //  create a loop function
    setTimeout(function() {   //  call a 3s setTimeout when the loop is called   //  your code here
      console.log('#feature'+j)
      $('#feature'+j).css('transform', 'translateY(0)')
      $('#feature'+j).css('opacity', 1)
      j++;                    //  increment the counter
      if (j < 5) {           //  if the counter < 10, call the loop function
        myLoopFeature();             //  ..  again which will trigger another
      }                       //  ..  setTimeout()
    }, 200)
  }




  var inView2 = false;

  function isScrolledIntoView(elem)
  {
    var docViewTop = $(window).scrollTop();
    var docViewBottom = docViewTop + $(window).height();

    var elemTop = $(elem).offset().top;
  var elemBottom = elemTop + $(elem).height();

  return ((elemTop <= docViewBottom) && (elemBottom >= docViewTop));
  }

  $(window).scroll(function() {
    if (isScrolledIntoView('#connecteddiv')) {
      if (inView2) { return; }
      inView2 = true;
      console.log('')
      textAnimate() ;
      // $('#connecteddivbtn').css('transition-duration', '1s')
      // $('#connecteddivbtn').css('opacity', 1)
    } else {
      inView2 = false;
    }
  });

  myLoopFeature()

})







var textWrapper = document.querySelector('.ml9 .letters');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

function textAnimate() {
  console.log('Calling Me')
  anime.timeline({loop: false})
    .add({
      targets: '.ml9 .letter',
      scale: [0, 1],
      duration: 500,
      elasticity: 10,
      delay: (el, i) => 45 * (i+1)
    })

  }

// Wrap every letter in a span
var textWrapper = document.querySelector('.ml12');
textWrapper.innerHTML = textWrapper.textContent.replace(/\S/g, "<span class='letter'>$&</span>");

anime.timeline({loop: true})
  .add({
    targets: '.ml12 .letter',
    translateX: [40,0],
    translateZ: 0,
    opacity: [0,1],
    easing: "easeOutExpo",
    duration: 1000,
    delay: (el, i) => 500 + 30 * i
  })
  .add({
    targets: '.ml12 .letter',
    translateX: [0,-30],
    opacity: [1,0],
    easing: "easeInExpo",
    duration: 1100,
    delay: (el, i) => 10000 + 30 * i
  });
