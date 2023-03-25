
window.addEventListener('scroll',
function(){
    let navbar=document.getElementById('nav-bar');
    if(this.window.pageYOffset>=411)
    {
        navbar.classList.add('sticky');
    }
    else{
        navbar.classList.remove('sticky');
    }
});

// displaying nepali date

let _mypatroDateFormat = 1;
let _mypatroResponseType = 'html';
let script = document.getElementById('display_date');
script.src = 'https://mypatro.com/resources/nepali_date/nepali_date.js';
document.head.appendChild(script);
