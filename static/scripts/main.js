var portfolio = {}

portfolio.DefaultView = Backbone.View.extend({
    el: 'body',
    events: { 
        'click .mobile-shade': 'closeMenu'
    },
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
                easing      : mina.elastic, 
                speed       : 600,
                size        : { w : 35, h : 35 },
                onToggle    : function() {

                    $('nav').toggleClass('animate-nav');
                    $('body').toggleClass('animate-body');
                    $('.mobile-menu').toggleClass('animate-body turn-white');
                    $('.mobile-shade').toggle();

                }
            } );
    },
    closeMenu: function() {
        $('.menu-toggle').trigger('click');
    },
    removeMobileStyles: function() {
        $('.mobile-shade').hide();

        var remove_classes  = ['animate-nav', 'animate-body', 'turn-white'],
            mobile_classes  = ['nav', 'body', '.mobile-menu'];

        _.each(mobile_classes, function(mClass) {

            // convert to jQuery object
            var thisClass = $(mClass);

            _.each(remove_classes, function(rClass) {
                if(thisClass.hasClass(rClass)) {
                    thisClass.removeClass(rClass);
                }
            });

        });
    }
});

portfolio.defaultview = new portfolio.DefaultView;

