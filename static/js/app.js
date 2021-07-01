const dashBoard = document.getElementById('dash');
const profileBtn = document.querySelectorAll('#full-profile');
const closeBtn = document.getElementById('close');


const fetchStudents = async () => {
  const response = await fetch('127.0.0.1:8000/studentsapi/students')
  const students = await response.json()
  return students;
}

profileBtn.forEach(element => {
  element.addEventListener("click", openDashboard);
  fetchStudents()
    .then(data => {
      console.log(data)
    })
    .catch(err => {
      console.log(err)
    });
  
})
closeBtn.addEventListener("click", closeDashboard);


function openDashboard(){
    dashBoard.classList.toggle('slow');
    dashBoard.classList.toggle('dash-close');
  
}
function closeDashboard(){
  dashBoard.classList.add('dash-close');
  
}



