$(document).ready(function() {
    var canvas = document.getElementById("canvas");
    if (canvas.getContext) {
        var ctx = canvas.getContext("2d");
        var blockSize = 40;
        var numRows = 10;
        var numCols = 15;

        for (var row = 0; row < numRows; row++) {
            for (var col = 0; col < numCols; col++) {
                var x = col * blockSize;
                var y = row * blockSize;
                ctx.fillStyle = getRandomColor();
                ctx.fillRect(x, y, blockSize, blockSize);
            }
        }
    }

    function getRandomColor() {
        var letters = "0123456789ABCDEF";
        var color = "#";
        for (var i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }
});
