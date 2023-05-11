/*  Navbar Responsive */

// function openNav(){
//     document.getElementById('nav').style.display = "block";
//     document.getElementById('close-btn').style.display = "block";
// }

// function closeNav(){
//     document.getElementById('nav').style.display = "none";
//     document.getElementById('close-btn').style.display = "none";
// }

let mydropdown_content = document.getElementById("myDropdown");
document.getElementById('dropbtn').addEventListener('click',()=>{
mydropdown_content.classList.toggle("show");
})

// Close the dropdown if the user clicks outside of it
window.onclick = function(e) {
  if (!e.target.matches('.dropbtn')) {
  var myDropdown = document.getElementById("myDropdown");
    if (myDropdown.classList.contains('show')) {
      myDropdown.classList.remove('show');
    }
  }

}
let toggleButton = document.querySelector('.toggle');
let nav = document.querySelector('.nav');

toggleButton.addEventListener('click', () => {
  nav.classList.toggle('active');
});

