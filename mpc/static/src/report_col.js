// get elements
var page = document.querySelector('.page');
var column = document.querySelector('.column');
var content = document.querySelector('.content');

// calculate height values of column and it's content
var columnHeight = column.offsetHeight;
var contentHeight = content.offsetHeight;

// create an array of offset values
var offsetValues = [];
for (var i = columnHeight; i < contentHeight; i+= columnHeight) {
    offsetValues.push(i);
}

// create a new column for each offset value
offsetValues.forEach( function(offsetValue, i) {

    // init clone and add classes
    var cloneColumn = document.createElement('div');
    var cloneContent = document.createElement('div');
    cloneColumn.classList.add('column');
    cloneContent.classList.add('content');
    
    // populate the DOM
    cloneContent.innerHTML = content.innerHTML;
    cloneColumn.appendChild(cloneContent);
    parent.appendChild(cloneColumn); 
    
    // apply position and offset styles
    cloneContent.style.position = 'relative';
    cloneContent.style.top = '-' + offsetValue + 'px';
});