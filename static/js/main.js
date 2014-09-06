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
			this.animate({'height':'345px'}, 600);
		} else {
			this.animate({'height':'50px'}, 600);
		}
	}

	/*
	 *
	 * Smoothen horizontal portfolio scroll and lazy load images
 	 * 
	 */
	$(function() {
		$('html, body').mousewheel(function(event, delta) {
		this.scrollLeft -= (delta * 10);
		// event.preventDefault();
		});
	});

	$('img.unveil').unveil();

});



var social = {}

social.Instagram = Backbone.Model.extend();

social.InstagramFeed = Backbone.Collection.extend({
	model: social.Instagram,
	url: 'https://api.instagram.com/v1/users/2968231/media/recent/?client_id=af80dd4c67de439fba77ac4c4743ead0',
	parse: function(response) {
		return response.results;
	},
	sync: function(method, model, options) {
		var params = _.extend({
			type: 'GET',
            dataType: 'jsonp',
            url: this.url,
            processData: false
		}, options);
		return $.ajax(params);
	}
});

social.InstagramView = Backbone.View.extend({
	el: '#social',
	feed: {},
	initialize: function() {
		this.collection = new social.InstagramFeed();
		this.fetchData();
		this.render();
	},
	render: function() {
		console.log(this.feed);
	},
	fetchData: function() {
		this.collection.fetch({
			success: function(collection, response) {

				// console.log(response);
				feed = response;
				// console.log(this.feed);

			},
			error: function() {
				console.log("failed to find instagram feed...");
			}
		});
	}
});

social.instagramview = new social.InstagramView;






