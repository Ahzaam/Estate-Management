

let profile = $('.profile')
for (let i = 0; i < profile.length +1; i++) {
  setTimeout(function() {
    $('#profile'+i).css('transform', 'scale(1.5)')
    $('#profile'+i).css('transform', 'translateX(0)')
    $('#profile'+i).css('opacity', 1)
  }, 1000)
}



let divs = $('.resource')

for (let i = 0; i < divs.length; i++) {
  setTimeout(function() {
    divs[i].style.transform = 'translateX(0)';
    divs[i].style.opacity = 1;
  }, 1000)
}

// document.querySelectorAll('.wish');
