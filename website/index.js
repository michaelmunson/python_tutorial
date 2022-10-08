

const h1El = document.querySelector("h1");

h1El.addEventListener("click", function(){
    this.style.color = "blue";
    this.innerHTML = '<a href="www.google.com"> Google </a>';
});

