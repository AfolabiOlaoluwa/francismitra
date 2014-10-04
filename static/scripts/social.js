var social = {}

/*
 *
 * MODELS
 *
 */
social.InstagramModel = Backbone.Model;

/*
 *
 * COLLECTIONS
 *
 */
social.InstagramCollection = Backbone.Collection.extend({
	model: social.InstagramModel,
	url: '/social/instagram',
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
			var photo   = this.feed[i].images.standard_resolution.url,
				caption = this.feed[i].caption == null ? '' : this.feed[i].caption.text,
				likes   = this.feed[i].likes.count,
				id      = this.feed[i].id;

			images[i]   = {'photo': photo, 'caption': caption, 'likes': likes, 'id': id};
		}

		var template = _.template($('#instagram-template').html());
		this.$el.html(template({ collection: images }));
	},
	fetchData: function() {
		var self = this;
		this.collection.fetch({
			success: function(collection, response) {
				if(response.result == 'success') {
					self.feed = response.content.data;
				} else {
					console.log(response)
				}
			},
			error: function() {
				console.log("Failure in BB object social.InstagramCollection");
			}
		});
	},
	likeMedia: function(e) {
		var media 	    = e.currentTarget,
			media_id    = media.getAttribute('data-id'),
			media_count = Number(media.getAttribute('data-likes')),
			media_like  = '/social/media_like?id=';

		var likeMediaSuccess = function() {
			var count = $(media).find('.likes');
			count.text(media_count+1);
		}

		var likeMediaFail = function() {
			var hover  = $(media).parent('.instagram-hover'),
			    notice = hover.siblings('.instagram-fail');

			notice.show().delay(700).fadeOut();
		}

		$.ajax({
			type: 'GET',
			dataType: 'json',
			url: media_like+media_id,
			success: function(data) {
				if(data.result == 'success') {
					likeMediaSuccess();
				} else if (data.result == 'fail') {
					console.log(data);
					likeMediaFail();
				}
			}
		});

	}
});

social.instagramview = new social.InstagramView;