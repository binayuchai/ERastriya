
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