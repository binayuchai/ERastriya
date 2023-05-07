/*  Navbar Responsive */

// function openNav(){
//     document.getElementById('nav').style.display = "block";
//     document.getElementById('close-btn').style.display = "block";
// }

// function closeNav(){
//     document.getElementById('nav').style.display = "none";
//     document.getElementById('close-btn').style.display = "none";
// }


let toggleButton = document.querySelector('.toggle');
let nav = document.querySelector('.nav');

toggleButton.addEventListener('click', () => {
  nav.classList.toggle('active');
});
