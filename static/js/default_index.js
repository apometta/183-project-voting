/**
 * Created by smend on 12/3/2016.
 */
// This is the js for the default/index.html view.
var app = function() {
    var self = {};
    Vue.config.silent = false; // show all warnings

    self.format_str_list = function(strlist) {
        console.log("strlist = " + strlist)
        var rawstr = strlist[0];
        rawstr = rawstr.replace("'", "");
        rawstr = rawstr.replace("\"", "");
        rawstr = rawstr.replace(", ", ",");
        var rawstrlist = rawstr.split(",");
        console.log("rawstrlist = " + rawstrlist);
        return rawstrlist;
    }

    //needed to check races because some can have multiple candidates selected
    self.contains_vote = function(race_id, person) {
        if (self.vue.user_election_votes[race_id] == null){
            return false;
        }
        else{
            if (typeof self.vue.user_election_votes[race_id] != "array" && typeof self.vue.user_election_votes[race_id] != "object") {
                self.vue.user_election_votes[race_id] = [self.vue.user_election_votes[race_id]]
            }
            return self.vue.user_election_votes[race_id].includes(person);
        }
    };

    //for local races that accept multiple candidates for a position
    self.toggle_vote = function(race_id, person) {
        if (self.vue.user_election_votes[race_id] == null){
            self.vue.user_election_votes[race_id] = [person];
        }
        else{
            if (typeof self.vue.user_election_votes[race_id] != "array" && typeof self.vue.user_election_votes[race_id] != "object") {
                self.vue.user_election_votes[race_id] = [self.vue.user_election_votes[race_id]]
            }
            if (!self.vue.user_election_votes[race_id].includes(person)) {
                self.vue.user_election_votes[race_id].push(person)
            }
            //toggle person off if they are already selected
            else {
                idx = self.vue.user_election_votes[race_id].indexOf(person);
                self.vue.user_election_votes[race_id].splice(idx, 1)
            }
        }
    };

    self.get_data = function() {
        //fetches election data and user information
        $.getJSON(data_url, function(data) {
            self.vue.current_user = data.current_user;
            self.vue.federal = data.national;
            self.vue.state_elections = data.state_races;
            self.vue.state_props = data.state_measures;
            self.vue.local_elections = data.local_races;
            self.vue.local_props = data.local_measures;
            if (data.votes_races.length > 0){
                self.vue.user_election_votes = JSON.parse(data.votes_races[0].votes_json);
            }
            if (data.votes_measures.length > 0){
                self.vue.user_prop_votes = JSON.parse(data.votes_measures[0].votes_json);
            }
        })
    };

    self.save_votes = function() {
        //sends user selected positions to db
        $.post(user_votes_url,
            {
                election_info: JSON.stringify(self.vue.user_election_votes),
                prop_info: JSON.stringify(self.vue.user_prop_votes),
            },
            function (data) {
                $.web2py.flash("Choices saved, remember to register to vote!");
            }
        );
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
            user_election_votes: [],
            user_prop_votes:[],
        },
        methods: {
            get_data: self.get_data,
            save_votes: self.save_votes,
            contains_vote: self.contains_vote,
            toggle_vote: self.toggle_vote,
            format_str_list: self.format_str_list,
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