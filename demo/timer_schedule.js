var schedule = require("node-schedule");

var rule = new schedule.RecurrenceRule();

var times = [];

for(var i=1; i<60; i++){
    times.push(i);
}

rule.second = times;

var c=0;

var j = schedule.scheduleJob("*/1 * * * *", function(){
    c++;
   console.log(new Date()); 
   console.log(c);
});

