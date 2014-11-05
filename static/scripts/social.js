var social = {}

/*
=================================================
MODELS
================================================*/
social.InstagramModel = Backbone.Model.extend({
	likeMedia: function(target) {
		var target       = target,
			media_id     = this.attributes.id,
			media_like   = '/social/media_like';

		var likeMediaSuccess = function(target, status) {
			var $target 	 = $(target),
				count  		 = $target.find('.likes'),
				media_count  = $target.data('likes'),
				status 		 = status;

			if(status == false) {
				count.text(media_count+1);
				var new_count = Number(count.text());

				media_count = $target.data('likes', new_count);
				// media_count = $target.attr('data-likes', new_count);
			} else {
				count.text(media_count-1);
				var new_count = Number(count.text());
				
				media_count = $target.data('likes', new_count);
				// media_count = $target.attr('data-likes', new_count);
			}


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
					likeMediaSuccess(target, data.previously_liked);
				} else if (data.result == 'fail') {
					console.log(data);
					likeMediaFail(target);
				}
			},
			error: function() {
				console.log("Failure in BB object social.InstagramModel");
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
	url: '/social/instagram',
	parse: function(response) {
		// Instagram model collection is returned under data
		return response.content.data;
	},
	sync: function(method, model, options) {
		var params = _.extend({
			type: 'GET',
            dataType: 'json',
            url: this.url,
		}, options);
		return $.ajax(params);
	}
});

/*
=================================================
VIEWS
================================================*/
social.InstagramView = Backbone.View.extend({
	el: '#social',
	query: {},
	cache: {},
	events: {
		'click .details': 'fireModel',
		'click #load-more': 'fetchData'
	},
	initialize: function() {
		this.collection = new social.InstagramCollection();

		this.collection.on('sync', this.render, this);

		this.fetchData();

		// Trigger a click event to auto load on scroll
		$(window).scroll(function() {
		   if($(window).scrollTop() + $(window).height() == $(document).height()) {
		   		$('#load-more').trigger('click');
		   }
		});

	},
	render: function() {
		var images = {};

		// var models = this.collection.models;

		// Parse Instagram collection
		for(var i = 0; i < this.cache.length; i++) {
			var photo   = this.cache[i].images.standard_resolution.url,
				caption = this.cache[i].caption == null ? '' : this.cache[i].caption.text,
				likes   = this.cache[i].likes.count,
				id      = this.cache[i].id;

			// Prep images object to dump on template
			images[i]   = {'photo': photo, 'caption': caption, 'likes': likes, 'id': id};
		}

		var holder 	 = $('#instagram-block'),
		    template = _.template($('#instagram-template').html());

		holder.append(template({ collection: images }));

	},
	fetchData: function() {
		var self = this;
		this.collection.fetch({
			remove: false,
			data: self.query,
			success: function(collection, response) {
				if(response.result == 'success') {

					// Store an reference of the most recently retrieved models
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
	fireModel: function(e) {
		var target	    = e.currentTarget,
			media_id    = target.getAttribute('data-id');

		var model = this.collection.findWhere({
			id: media_id
		});

		model.likeMedia(target);
	},
});

social.instagramview = new social.InstagramView;