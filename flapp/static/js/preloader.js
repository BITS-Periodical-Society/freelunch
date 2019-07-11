$(window).on('load', function() { // makes sure the whole site is loaded 
  $('main').fadeOut(); // will fade out the white DIV that covers the website. 
  $('#site').css('display', 'block');
  sr.reveal($('article#animate'), {
          duration: 2000,
          origin:'right',
          distance:'300px'
        });
})