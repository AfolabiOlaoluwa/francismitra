var blog = {}

/*
=================================================
MODELS
================================================*/
blog.BlogModel = Backbone.Model;

/*
=================================================
COLLECTIONS
================================================*/
blog.BlogCollection = Backbone.Collection.extend({
    model: blog.BlogModel,
    url: '/blog/api'
});

/*
=================================================
VIEWS
================================================*/
blog.BlogView = Backbone.View.extend({
    el: '#blog',
    page: 1,
    template: _.template($('#blog-template').html()),
    events: {
        'click #load-more': 'fetchCollection'
    },
    initialize: function() {
        this.collection = new blog.BlogCollection();

        this.collection.on('sync', this.render, this);

        this.collection.fetch();
    },
    render: function() {

        if(_.isEmpty(this.collection.models)) {
            $('#load-more').text('No New Content');
        }

        var holder = $('#blog-view');
        var date = new Date();
        var monthNames = [ "Null", "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December" ];

        _.each(this.collection.models, function(model) {

            var old_date = model.attributes.created;
            var split    = old_date.split("-");

            var year  = split[0];
            var month = Number(split[1]);
            var day   = split[2].substring(0, 2);

            var new_date = monthNames[month] + " " + day + ", " + year;
            
            model.set('created', new_date);
        });

        holder.append(this.template({ collection: this.collection.toJSON() }));

        $('img.unveil').unveil();

    },
    fetchCollection: function(e) {

        this.page = this.page + 1;
        this.collection.fetch({data: { page: this.page }});

    }
});

blog.blogView = new blog.BlogView;