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

	var Menu = function() {
		this.min_height = '50px';
		this.max_height = '380px';
		this.speed		= 600;
	};

	Menu.prototype = {
		animateMenu: function(items) {
			var speed 		= this.speed,
				max_height	= this.max_height,
				min_height	= this.min_height;

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
	};

}(window.jQuery, window, document));

