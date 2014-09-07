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

/*
 *
 * MODELS
 *
 */
social.Instagram = Backbone.Model.extend();

/*
 *
 * COLLECTIONS
 *
 */
social.InstagramFeed = Backbone.Collection.extend({
	model: social.Instagram,
	url: 'https://api.instagram.com/v1/users/2968231/media/recent/?client_id=af80dd4c67de439fba77ac4c4743ead0',
	parse: function(response) {
		return response;
		// return response.results;
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

/*
 *
 * VIEWS
 *
 */
social.InstagramView = Backbone.View.extend({
	el: '#social',
	feed: {},
	initialize: function() {
		this.collection = new social.InstagramFeed();

		this.collection.on('sync', this.render, this);

		this.fetchData();
	},
	render: function() {
		var images = {};

		for(var i = 0; i < this.feed.length; i++) {
			var photo = this.feed[i].images.standard_resolution.url;
			var caption = this.feed[i].caption == null ? 'no caption' : this.feed[i].caption.text;
			var likes = this.feed[i].likes.count;
			var id = this.feed[i].id;

			images[i] = {'photo': photo, 'caption': caption, 'likes': likes, 'id': id};
		}

		var template = _.template($('#instagram-template').html());
		this.$el.html(template({ collection: images }));

	},
	fetchData: function() {
		var self = this;
		this.collection.fetch({
			success: function(collection, response) {
				self.feed = response.data;
			},
			error: function() {
				console.log("failed to find instagram feed...");
			}
		});
	}
});

social.instagramview = new social.InstagramView;






