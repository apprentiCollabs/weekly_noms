$(document).ready(function() {
    function addDrag() {
        var talks = Array.prototype.slice.call(document.querySelectorAll(".category"));
        var recipes = Array.prototype.slice.call(document.querySelectorAll(".indRecipe"));
        var containers = talks.concat(recipes);

        dragula(containers).on('drop', function(el, target, source, sibling) {
            if (target.classList.contains('recipes')) {
                // hide drag & drop hint
                target.firstChild.data = '';
                target.style.border = '';
            }
        })

        if (source.classList.contains('session-talks')) {
            // restore drag & drop hint
            if (source.childNodes.length == 1) {
            source.firstChild.data = 'Drag talks here';
            }
        }
    }
})
