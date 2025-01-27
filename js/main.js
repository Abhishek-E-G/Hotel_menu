(function($) {

	"use strict";

	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	var carousel = function() {
		$('.home-slider').owlCarousel({
	    loop:true,
	    autoplay: true,
	    margin:0,
	    animateOut: 'fadeOut',
	    animateIn: 'fadeIn',
	    nav:true,
	    dots: true,
	    autoplayHoverPause: false,
	    items: 1,
	    navText : ["<span class='ion-ios-arrow-back'></span>","<span class='ion-ios-arrow-forward'></span>"],
	    responsive:{
	      0:{
	        items:1
	      },
	      600:{
	        items:1
	      },
	      1000:{
	        items:1
	      }
	    }
		});

	};
	carousel();

})(jQuery);


// moving box

const box = document.querySelector('.box');

let positionX = 0;
const step = 1; // Smaller step for slower movement
const screenWidth = window.innerWidth;
const boxWidth = box.offsetWidth;

function moveBox() {
  positionX += step;

  if (positionX > screenWidth) {
    positionX = -boxWidth; // Start from the left side again
  }

  box.style.transform = `translateX(${positionX}px)`;

  requestAnimationFrame(moveBox);
}

moveBox();


