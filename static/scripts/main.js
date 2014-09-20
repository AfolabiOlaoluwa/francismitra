(function($, window, document) {

	$(function() {

		var menu = new Menu();

		$('html, body').mousewheel(function(event, delta) {
			this.scrollLeft -= (delta * 10); 
		});
		$('img.unveil').unveil();

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
				max_height  = '345px';

			// Animate each item in array
			for (var i = 0; i < items.length; i++) {

				var item   = $(items[i]),
					height = item.css('height');

				if(height == min_height) {
					item.animate({'height': max_height}, 600);
				} else {
					item.animate({'height': min_height}, 600);
				}

			}

		}
	}

}(window.jQuery, window, document));

