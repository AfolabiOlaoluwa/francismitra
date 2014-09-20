(function($, window, document) {

	$(function() {

		// Enable horizontal scrolling on portfolio
		$('html, body').mousewheel(function(event, delta) {
			this.scrollLeft -= (delta * 10); 
		});

		// Lazy load images
		$('img.unveil').unveil();

		var menu = new Menu();

		new svgIcon( document.querySelector( '.menu-toggle' ), 
			svgIconConfig, { 
				easing		: mina.elastic, 
				speed		: 600,
				size		: { w : 35, h : 35 },
				onToggle	: function() {

					var nav 	  = document.querySelector('nav');
						nav_push  = document.querySelector('.nav-push'),
						toAnimate = [nav, nav_push];

					menu.animateMenu(toAnimate);

				}
			} );

	});

	function Menu() {

		this.animateMenu = function(items) {

			// Default values
			var	min_height  = '50px',
				max_height  = '380px',
				speed 		= 600;

			// Animate each item in array
			for (var i = 0; i < items.length; i++) {

				var item   = $(items[i]),
					height = item.css('height');

				if(height == min_height) {
					item.animate({'height': max_height}, speed);
				} else {
					item.animate({'height': min_height}, speed);
				}

			}

		}
	}

}(window.jQuery, window, document));

