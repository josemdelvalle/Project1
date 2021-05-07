employeeId = null;
_name = null;
lastName = null;
role = null;
department = null;
urgent = false;
reimburstment = 1000;

var xhr = new XMLHttpRequest();
const btn = document.getElementById('loginButton');
btn.addEventListener('click', (e) => {
  e.preventDefault(); // disable the refresh on the page when submit
  const username = document.getElementById('usernameInput').value;
  const password = document.getElementById('passwordInput').value;
  //var xhr = new XMLHttpRequest();
  xhr.open("POST", "http://localhost:5000/login", true);
  // xhr.withCredentials = true;
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify({
    userName: username,
    password: password
  }));
  xhr.onload = function () {
    var data = JSON.parse(this.responseText);
    if (data.employeeId) {
      employeeId = data.employeeId;
      _name = data.name;
      lastName = data.lastName;
      role = data.role;
      department = data.department;
      document.getElementById("loginMessage").innerHTML = "<br>Logged in";
      document.getElementById("displayName").innerHTML = _name;
      document.getElementById("displayRole").innerHTML = role;
      append = document.getElementById("courseTableBody").innerHTML = "";
    }

    console.log(data);
    console.log(employeeId);

  }
});
const logOutBtn = document.getElementById('logOut');
logOutBtn.addEventListener('click', (e) => {
  e.preventDefault();
  employeeId = null;
  _name = null;
  lastName = null;
  role = null;
  department = null;
  document.getElementById("loginMessage").innerHTML = "<br>Logged out";
  append = document.getElementById("courseTableBody").innerHTML = "";
});

function swicthTab(evt, currentTab) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  document.getElementById(currentTab).style.display = "block";
}







const addCourseBtn = document.getElementById('submitCourseBtn');
addCourseBtn.addEventListener('click', (e) => {
  e.preventDefault(); // disable the refresh on the page when submit
  const date = document.getElementById('startDate').value;
  const time = document.getElementById('courseTime').value;
  const location = document.getElementById('inputLocation').value;
  const description = document.getElementById('description').value;
  const cost = document.getElementById('inputCost').value;
  const gradingFormat = document.getElementById('gradingFormat').value;
  const eventType = document.getElementById('eventType').value;
  const gradeRequired = document.getElementById('requiredGrade').value;
  const workJustification = document.getElementById('workJustification').value;

  var date1 = new Date();
  var date2 = new Date(date);
  var Difference_In_Time = date2.getTime() - date1.getTime();
  var Difference_In_Days = Difference_In_Time / (1000 * 3600 * 24);
  if (Difference_In_Days <= 14) {
    console.log(Difference_In_Days)
    urgent = true;
  }else{
    urgent=false
  }
    
    var xhhr = new XMLHttpRequest();
    xhhr.open("POST", "http://localhost:5000/addCourse", true);
    xhhr.setRequestHeader('Content-Type', 'application/json');

    xhhr.send(JSON.stringify({
      date: date,
      time: time,
      location: location,
      description: description,
      cost: cost,
      gradingFormat: gradingFormat,
      eventType: eventType,
      gradeRequired: gradeRequired,
      workJustification: workJustification,
      employeeId: employeeId,
      urgent: urgent
    }));
    xhhr.onload = function () {
      var data = JSON.parse(this.responseText);
      console.log(data);
      document.getElementById('subitCourseMessage').innerHTML=data[0];
    }
  


});














const getCourseBtn = document.getElementById('getCoursesBtn');
getCourseBtn.addEventListener('click', (e) => {
  e.preventDefault(); // disable the refresh on the page when submit

  console.log(role);
  console.log(department);
  var xhhr = new XMLHttpRequest();
  xhr.open("POST", "http://localhost:5000/getCourses", true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify({
    employeeId: employeeId,
    role: role,
    department: department

  }));

  function checkMark(x) {
    if (x == null) {
      return "&#9744"

    } else if (x == true) {
      return "&#x2611;";
    } else {
      return "&#x2612";
    }
  };
  xhr.onload = function () {
    reimburstment=1000;
    var data = JSON.parse(this.responseText);
    console.log(data);
    append = document.getElementById("courseTableBody");
    if (this.readyState == 4 && this.status == 200) {
      if (data) {
        append.innerHTML = "";
        for (let i = 0; i < data.length; i++) {
          x = "Pending";
          urgentColor = "black"

          if (data[i].urgent == true) {
            urgentColor = "red";
          }
          if (data[i].grade != null) {
            x = data[i].grade;
          }
          if (data[i].employeeId == employeeId) {
            switch (data[i].eventType) {
              case "University Course":
                reimburstment = reimburstment - data[i].cost * .8;
                break;
              case "Seminar":
                reimburstment = reimburstment - data[i].cost * .6;

                break;
              case "Certification Preparation Class":
                reimburstment = reimburstment - data[i].cost * .75;

                break;
              case "Certification":
                reimburstment = reimburstment;

                break;
              case "Technical Training":
                reimburstment = reimburstment - data[i].cost * .9;

                break;
              case 1:
                reimburstment = reimburstment - data[i].cost * .3;

                break;
              default:
                text = "No value found";
            }
          }


          append.innerHTML += `<tr>
          <td>${data[i].courseId}</td>
          <td>${data[i].date}</td>
          <td>${data[i].time}</td>
          <td>${data[i].location}</td>
          <td>${data[i].description}</td>
          <td>${data[i].cost}</td>
          <td>${data[i].gradingFormat}</td>
          <td>${data[i].eventType}</td>
          <td>${data[i].gradeRequired}</td>
          <td style="color:${urgentColor}">${data[i].urgent}</td>
          <td>${x}</td>
          <td>${data[i].workJustification}</td>
          <td>${data[i].employeeId}</td>
          <td>${checkMark(data[i].supervisorApproval)} , ${checkMark(data[i].departmentHeadApproval)}, ${checkMark(data[i].bencoApproval)} </td>
          <td><button type="button" class="rejectButn btn btn-danger"  value="${data[i].courseId}">x</button></td>
          </tr>`;
        }

        document.getElementById("displayReimburstment").innerHTML =reimburstment;
        let rejectButnArray = document.querySelectorAll(".rejectButn");
        rejectButnArray.forEach(function (elem) {
          elem.addEventListener('click', (e) => {
            e.preventDefault(); // disable the refresh on the page when submit
            coursetodelete = elem.getAttribute('value');
            xhr.open("PUT", "http://localhost:5000/approveCourse", true);
            xhr.setRequestHeader('Content-Type', 'application/json');
            xhr.send(JSON.stringify({
              employeeId: employeeId,
              role: role,
              courseId: coursetodelete,
              approval: false
            }));
            xhr.onload = function () {
              var data = JSON.parse(this.responseText);
              console.log(data);
              append = document.getElementById("courseTableBody");
              if (this.readyState == 4 && (this.status == 200 || 204)) {
                console.log(data);
              }
            }


          });
        });

      }
    }

  }

});

const approveCourseBtn = document.getElementById('approveCourseBtn');
approveCourseBtn.addEventListener('click', (e) => {
  e.preventDefault(); // disable the refresh on the page when submit
  const approveCourseInput = document.getElementById('approveCourseInput').value;
  console.log(approveCourseInput);
  xhr.open("PUT", "http://localhost:5000/approveCourse", true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.send(JSON.stringify({
    employeeId: employeeId,
    role: role,
    courseId: approveCourseInput,
    approval: true
  }));
  xhr.onload = function () {
    var data = JSON.parse(this.responseText);
    console.log(data);
    append = document.getElementById("courseTableBody");
    if (this.readyState == 4 && (this.status == 200 || 204)) {
      console.log(data);
    }
  }

});