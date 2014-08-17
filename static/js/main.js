$(document).ready(function() {
	
	/*
	 *
	 * Initialize svg icon
	 *
	 */
	(function() {

		new svgIcon( document.querySelector( '.menu-toggle' ), 
			svgIconConfig, { 
				easing		: mina.elastic, 
				speed		: 600,
				size		: { w : 35, h : 35 },
				onToggle	: function() {

					$('nav').animateMenu();
					$('.nav-push').animateMenu();

				}
			} );

	})();

	/*
	 *
	 * Animations for mobile menu
 	 * 
	 */
	$.fn.animateMenu = function() {
		var height = this.css('height');
		if(height == '50px') {
			this.animate({'height':'370px'}, 600);
		} else {
			this.animate({'height':'50px'}, 600);
		}
	}

	/*
	 *
	 * Smoothen horizontal portfolio scroll
 	 * 
	 */
	$(function() {
		$('html, body').mousewheel(function(event, delta) {
		this.scrollLeft -= (delta * 10);
		// event.preventDefault();
		});
	});


});