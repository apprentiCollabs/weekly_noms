$(document).ready(function() {
    // make add new ingredient column div appear
    $("button#addIngredTrigger").click(function(){
        $("aside#addIngredCol").toggle();
    });

    $("span#addNew").click(function(){
        newElement();
    });

    // what happens when you click add on the new ingredient input
    function newElement() {
        // get all close buttons
        var allCloseBtns = document.getElementsByClassName("closeBtn");

        // creates new li and adds class
        var newLi = document.createElement("li");
        newLi.className = 'userAddedIngred';

        // get value from input box, makes it into a text node, and adds it to the newly created li
        var inputValue = document.getElementById("newIngredInput").value;
        var newIngredText = document.createTextNode(inputValue);
        newLi.appendChild(newIngredText);

        // handles error of blank input
        if (inputValue === '') {
            alert("You must write something!");
        }
        else {
            document.getElementById("addedItems").appendChild(newLi);
        }

        // sets input to be blank
        document.getElementById("newIngredInput").value = "";

        // creates close buttons and appends them to newly added ingredients
        var closeBtnSpan = document.createElement("span");
        var closeButtonText = document.createTextNode("\u00D7");
        closeBtnSpan.className = "closeBtn";
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

    // gives close buttons functionality to remove items from list
    // var closeBtns = document.getElementsByClassName("closeBtn");

    // create new ingredient from user input
    // function addNewIngred() {
        // creates new li and add class
        // var newLi = document.createElement('li');
        // li.className = 'newlyAdded';

        // get value from user input and create text node, which is added to the new list item
        // var inputValue = document.getElementById('newIngredInput').value;
        // var newIngredText = document.createTextNode(inputValue);
        // newLi.appendChild(newIngredText);

        // deals with blank inputs added by accident
        // if (inputValue === '') {
        //     alert('New ingredient name cannot be blank.');
        // }
        // else {
        //     document.getElementById('addedItems').appendChild(nnewLi);
        // }

        // resets new ingredient input to blank
        // document.getElementById('newIngredInput').value = '';

        // creates close buttons and appends to new ingredient list items
        // var closeBtnSpan = document.createElement('span');
        // var closeBtnText = document.createTextNode('\u00D7');
        // closeBtnSpan.className = 'close';
        // closeBtnSpan.appendChild(closeBtnText);
        // newLi.appendChild(closeBtnSpan);

        // makes close buttons remove items
//         for (var i = 0; i < closeBtns.length; i++) {
//             closeBtns[i].onclick = function() {
//                 var actualLi = document.getElementsByClassName('ingredListItem');
//                 actualLi.remove();
//             }
//         }
//     }
})
