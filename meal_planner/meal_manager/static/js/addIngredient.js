$(document).ready(function() {
    // make add new ingredient column div appear
    $('button#addIngredTrigger').click(function(){
        $('aside#addIngredCol').toggle();
    });

    // add click listener on add new button, invokes function below
    $('span#addNew').click(function(){
        newElement();
    });

    function newElement() {
        // get all close buttons
        var allCloseBtns = document.getElementsByClassName('closeBtn');

        // creates new li and adds class
        var newLi = document.createElement('li');
        newLi.className = 'userAddedIngred';

        // get value from input box, makes it into a text node, and adds it to the newly created li
        var inputValue = document.getElementById('newIngredInput').value;
        var newIngredText = document.createTextNode(inputValue);
        newLi.appendChild(newIngredText);

        // handles error of blank input
        if (inputValue === '') {
            alert('You must write something!');
        }
        else {
            document.getElementById('addedItems').appendChild(newLi);
        }

        // sets input to be blank
        document.getElementById('newIngredInput').value = '';

        // creates close buttons and appends them to newly added ingredients
        var closeBtnSpan = document.createElement('span');
        var closeButtonText = document.createTextNode('\u00D7');
        closeBtnSpan.className = 'closeBtn';
        closeBtnSpan.appendChild(closeButtonText);
        newLi.appendChild(closeBtnSpan);

        // adds functionality for close buttons
        for (var i = 0; i < allCloseBtns.length; i++) {
            allCloseBtns[i].onclick = function() {
                var newIngredLi = this.parentElement;
                newIngredLi.remove();
            }
        }
    }
})
