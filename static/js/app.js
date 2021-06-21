const dashBoard = document.getElementById('dash');
const profileBtn = document.querySelectorAll('#full-profile');
const closeBtn = document.getElementById('close');

profileBtn.forEach(element => {
   element.addEventListener("click", openDashboard);
})
closeBtn.addEventListener("click", closeDashboard);

function openDashboard(){
    dashBoard.classList.toggle('slow');
    dashBoard.classList.toggle('dash-close');
  
}
function closeDashboard(){
  dashBoard.classList.add('dash-close');

}

