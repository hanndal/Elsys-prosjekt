var canvasS = 400;
var houseW = 15.5;
var stoneD = 1;

const positionData = fetch("http://localhost:8000/position.json")
  .then((response) => response.json())
  .then((x) => {

    return x;
  });

const drawStone = () => {
    positionData.then((pos) => { 
         
        var aR = canvasS/3000;
        var posX = pos.x * aR;
        var posY = pos.y * aR;

        fill("magenta");
        pixRad = canvasS * (stoneD / houseW);
        circle(posX, posY, pixRad);
    });
  };

function drawCircles() {

    var i;
    var j = 12;
    var aR;
    var pixRad;

    var colourA = ["blue", "white", "red"];

    for (i = 0; i < 3; i++) {

        pixRad = canvasS * (j / houseW);
        fill(colourA[i]);
        circle(canvasS/2, canvasS/2, pixRad);

        j-=4;
    }
    
    pixRad = canvasS * (1 / houseW);
    fill("white");
    circle(canvasS/2, canvasS/2, pixRad);
  };

function setup(){
    var canvas = createCanvas(canvasS, canvasS);
    canvas.parent('canvasID');

    noStroke(); 
}

function draw(){
    background(255);
    drawCircles();
    drawStone(); 
}

