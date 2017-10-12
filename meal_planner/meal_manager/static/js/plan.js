$(document).ready(function() {
    function $(id) {
        return document.getElementById(id);
    }

    dragula([$('availableRecipes'), $('sunday'), $('monday'), $('tuesday'), $('wednesday'), $('thursday'), $('friday'), $('saturday'),], { revertOnSpill: true
    }).on('drop', function(el) {

    });
})
