var social = {}

/*
 *
 * MODELS
 *
 */
social.InstagramModel = Backbone.Model.extend();

/*
 *
 * COLLECTIONS
 *
 */
social.InstagramCollection = Backbone.Collection.extend({
	model: social.InstagramModel,
	url: 'http://127.0.0.1:8000/social/instagram',
	parse: function(response) {
		return response;
	},
	sync: function(method, model, options) {
		var params = _.extend({
			type: 'GET',
            dataType: 'json',
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
	events: {
		'click .details': 'likeMedia'
	},
	initialize: function() {
		this.collection = new social.InstagramCollection();

		this.collection.on('sync', this.render, this);

		this.fetchData();
	},
	render: function() {
		var images = {};

		for(var i = 0; i < this.feed.length; i++) {
			var photo   = this.feed[i].images.standard_resolution.url;
			var caption = this.feed[i].caption == null ? '' : this.feed[i].caption.text;
			var likes   = this.feed[i].likes.count;
			var id      = this.feed[i].id;

			images[i]   = {'photo': photo, 'caption': caption, 'likes': likes, 'id': id};
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
	},
	likeMedia: function(e) {
		// var media_id = e.getAttribute('data-id');
		var media 	    = e.currentTarget;
		var media_id    = media.getAttribute('data-id');
		var media_count = Number(media.getAttribute('data-likes'));
		var media_like  = 'http://127.0.0.1:8000/social/media_like?id='

		var likeMediaSuccess = function() {
			var count = $(media).find('.likes');
			count.text(media_count+1);
		}

		$.ajax({
			type: 'GET',
			dataType: 'json',
			url: media_like+media_id,
			success: function(data) {
				likeMediaSuccess();
				// console.log(data);
			}
		});

	}
});

social.instagramview = new social.InstagramView;