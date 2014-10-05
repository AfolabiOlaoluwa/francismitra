var portfolio = {}

portfolio.DefaultView = Backbone.View.extend({
	el: 'body',
	initialize: function() {
		var self = this;

		// Enable horizontal scrolling on portfolio
		$('html, body').mousewheel(function(event, delta) {
			this.scrollLeft -= (delta * 10); 
		});

		// Lazy load images
		$('img.unveil').unveil();

		// Initialize animated menu icon
		new svgIcon( document.querySelector( '.menu-toggle' ), 
			svgIconConfig, { 
				easing		: mina.elastic, 
				speed		: 600,
				size		: { w : 35, h : 35 },
				onToggle	: function() {

					$('nav').toggleClass('animate-nav');
					$('body').toggleClass('animate-body');
					$('.mobile-menu').toggleClass('animate-body turn-white');
					$('.mobile-shade').toggle();
					// var nav 	  = document.querySelector('nav');
					// 	nav_push  = document.querySelector('.nav-push'),
					// 	toAnimate = [nav, nav_push];

					// self.animateMenu(toAnimate);

				}
			} );
	},
	// Depreciated animation used for dropdown menu
	animateMenu: function(items) {
		var speed 		= 600,
			max_height	= '380px',
			min_height	= '50px';

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
});

portfolio.defaultview = new portfolio.DefaultView;

