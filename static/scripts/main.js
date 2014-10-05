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

		// Check to close mobile menu if open on desktop view
		window.addEventListener('resize', function() {
			if(document.documentElement.clientWidth > 768) {
				self.removeMobileStyles();
			}
		});

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

				}
			} );
	},
	removeMobileStyles: function() {
		$('.mobile-shade').hide();

		var remove_classes  = ['animate-nav', 'animate-body', 'turn-white'],
			mobile_classes  = ['nav', 'body', '.mobile-menu'];

		for (var i = 0; i < mobile_classes.length; i++) {
			// convert to a jQuery object
			var thisClass = $(mobile_classes[i]);

			for (var c = 0; c < remove_classes.length; c++) {
				if(thisClass.hasClass(remove_classes[c])) {
					thisClass.removeClass(remove_classes[c]);
				}
			}

		}

	}
});

portfolio.defaultview = new portfolio.DefaultView;

