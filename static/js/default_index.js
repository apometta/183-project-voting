/**
 * Created by smend on 12/3/2016.
 */
// This is the js for the default/index.html view.
var app = function() {
    var self = {};
    Vue.config.silent = false; // show all warnings

    self.get_data = function() {
        //fetches election data and user information
    };

    self.save_votes = function() {
        //sends user selected positions to db
    };

    // Complete as needed.
    self.vue = new Vue({
        el: "#vue-div",
        delimiters: ['${', '}'],
        unsafeDelimiters: ['!{', '}'],
        data: {
            current_user: null,
            federal: [],
            state_elections: [],
            state_props: [],
            local_elections: [],
            local_props: [],
        },
        methods: {
            get_data: self.get_data,
            save_votes: self.save_votes,
        }

    });

    self.get_data();
    $("#vue-div").show();

    return self;
};

var APP = null;

// This will make everything accessible from the js console;
// for instance, self.x above would be accessible as APP.x
jQuery(function(){APP = app();});