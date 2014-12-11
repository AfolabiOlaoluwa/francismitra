var social = {}

/*
=================================================
MODELS
================================================*/
social.InstagramModel = Backbone.Model.extend({
	likeMedia: function(model, target) {

		var model = model;
		var media_like = '/social/media_like';
		var media_id = model.get('id');
		var target = target;

		var likeMediaSuccess = function(model, status) {
			var status = status;
			var model = model;

			// Dealing with Backbone's sync issues on nested fields 
			var clonedModel = _.clone(model.get('likes'));

			status == false ?  clonedModel.count + 1 : clonedModel.count - 1;

			model.set('likes', clonedModel);
		}

		var likeMediaFail = function(target) {
			var target = target,
				hover  = $(target).parent('.instagram-hover'),
			    notice = hover.siblings('.instagram-fail');

			notice.show().delay(700).fadeOut();
		}

		$.ajax({
			type: 'GET',
			dataType: 'json',
			url: media_like,
			data: {'id':media_id},
			success: function(data) {
				if(data.result == 'success') {
					// console.log(data);
					likeMediaSuccess(model, data.previously_liked);
				} else if (data.result == 'fail') {
					// console.log(data);
					likeMediaFail(target);
				}
			},
			error: function() {
				console.log('Failure in BB object social.InstagramModel');
			}
		});

	}
});

/*
=================================================
COLLECTIONS
================================================*/
social.InstagramCollection = Backbone.Collection.extend({
	model: social.InstagramModel,
	cache: {},
	url: '/social/instagram',
	parse: function(response) {
		// Instagram model collection is returned under data
		return response.content.data;
	},
	fetchData: function() {
		var self = this;
		this.fetch({
			remove: false,
			data: self.query,
			success: function(collection, response) {
				if(response.result == 'success') {

					// Store a reference of the most recently retrieved models
					self.cache = response.content.data;

					var max_id = response.content.pagination.next_max_id;
					self.query = {'max_id':max_id};

					// console.log(response.content.data);

				} else {
					console.log(response)
				}
			},
			error: function() {
				console.log("Failure in BB object social.InstagramCollection");
			}
		});
	},
});

/*
=================================================
VIEWS
================================================*/
social.InstagramView = Backbone.View.extend({
	el: '#social',
	query: {},
	events: {
		'click .details': 'fireModel',
		'click #load-more': 'fetchCollection'
	},
	initialize: function() {
		this.collection = new social.InstagramCollection();

		this.collection.on('sync', this.render, this);

		this.collection.fetchData();
	},
	render: function() {

		var images = {};

		// Parse Instagram collection
		for(var i = 0; i < this.collection.cache.length; i++) {
			var photo   = this.collection.cache[i].images.standard_resolution.url,
				caption = this.collection.cache[i].caption == null ? '' : this.collection.cache[i].caption.text,
				likes   = this.collection.cache[i].likes.count,
				id      = this.collection.cache[i].id;

			// Prep images object to dump on template
			images[i]   = {'photo': photo, 'caption': caption, 'likes': likes, 'id': id};
		}

		var holder 	 = $('#instagram-block'),
		    template = _.template($('#instagram-template').html());

		holder.append(template({ collection: images }));

	},
	fetchCollection: function() {
		this.collection.fetchData();
	},
	fireModel: function(e) {
		var target	    = e.currentTarget,
			media_id    = target.getAttribute('data-id');

		var model = this.collection.findWhere({
			id: media_id
		});

		model.likeMedia(model, target);

	},
});

social.instagramview = new social.InstagramView;