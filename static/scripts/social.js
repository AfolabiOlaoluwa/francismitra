var social = {}

/*
=================================================
MODELS
================================================*/
social.InstagramModel = Backbone.Model.extend({
	likeMedia: function(model, target) {

		var model      = model,
			target     = target,
			media_like = '/social/media_like';

		var media_id = model.get('id');

		var likeMediaSuccess = function(model, status) {

			var status = status,
				model  = model;

			// Dealing with Backbone's sync issues on nested fields 
			var clonedModel = _.clone(model.get('likes'));

			status == false ? clonedModel.count + 1 : clonedModel.count - 1;

			model.set('likes', clonedModel);

			// var test = model.hasChanged('likes');
			// console.log(test);

			// model.on('change', function() {
			// 	console.log('something happened');
			// });

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
	quer: {},
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

					// Reset cache to prevent repeated models during pagination
					self.cache = new social.InstagramCollection(response.content.data);

					var max_id = response.content.pagination.next_max_id;
					self.query = {'max_id':max_id};

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
social.InstagramModelView = Backbone.View.extend({
	tagName: 'div',
	className: 'instagram-wrapper',
	template: _.template($('#instagram-template').html()),
	events: {
		'click .details': 'fireModel',
	},
    render: function() {

    	this.$el.html(this.template(this.model.toJSON()));

		return this;

    },
    fireModel: function() {

    	// var target	    = e.currentTarget,
    		// media_id    = target.getAttribute('data-id');

    	// var model = this.model.findWhere({
    		// id: media_id
    	// });

		console.log('clicked');

    	// model.likeMedia(model, target);
    },
});



social.InstagramView = Backbone.View.extend({
	el: '#social',
	events: {
		'click #load-more': 'fetchCollection'
	},
	initialize: function() {
		this.collection = new social.InstagramCollection();

		this.collection.on('sync', this.render, this);

		this.collection.fetchData();
	},
	render: function() {

		var buffer = document.createDocumentFragment(),
			holder = $('#instagram-block');

		_.each(this.collection.cache.models, function(thisModel) {

			if(thisModel.attributes.caption == null) {
				var cloned = _.clone(thisModel.get('caption'));

				cloned = {};
				cloned.text = '';

				thisModel.set('caption', cloned);
			}

			var modelView = new social.InstagramModelView({model: thisModel});
			buffer.appendChild(modelView.render().el);

		});

    	holder.append(buffer);
    	buffer = '';

	},
	fetchCollection: function() {
		this.collection.fetchData();
	},
});

social.instagramView = new social.InstagramView;



